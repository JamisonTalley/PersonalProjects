#segmentationClass.py
#Jamison Talley
#12-12-23

# import necessary libraries
import numpy as np

class segmentationClass():
    # class initializer that also defines hyperparameters
    def __init__(self):
        self.p0 = 1
        self.x_a = [0,0]
        self.x_b = [0,1]
        return

    # segmentImage method that takes an nxnx3 numpy array as input,
    # and returns an nxnx1 numpy array
    def segmentImage(self, I):
        # calculate value of n and calculate the number of nodes in the flow graph
        n = len(I)
        nodes = (n * n) + 2
        # calls constructAdjacencyMatrix method to create the flow network
        # adjacency matrix, and calls matrix_dfs method to find a path from
        # the source node to the sink node
        matrix = self.constructAdjacencyMatrix(I)
        path = self.matrix_dfs(matrix, nodes - 2, nodes - 1)

        # continually calls the ford_fulk method until there is no longer
        # a path from the source to the sink in the graph
        while path[len(path) - 1] == nodes - 1:
            matrix = self.ford_fulk(matrix, path)
            path = self.matrix_dfs(matrix, nodes - 2, nodes - 1)

        # creates an nxnx1 numpy array to store the binary segmentation
        out_image  = np.zeros([n,n,1])
        for i1 in range(1, len(path)):
            index = path[i1]
            out_image[index // n][index % n] = 1

        #returns binary segmentation
        return out_image
    
    # constructAdjacencyMatrix method that takes an nxnx3 matrix as input,
    # and returns an (n^2 + 2) X (n^2 + 2) numpy array
    # source is node n^2, and sink is node n^2 + 1
    def constructAdjacencyMatrix(self, I):
        #calculate value of n, and the number of pixels in the image
        n = len(I)
        pixels = (n * n)

        # creates an n^2x3 array to unravel the image
        I_list = []
        for i1 in range(n):
            for i2 in range(n):
                I_list.append(I[i1][i2])

        # unravels values of x_a and x_b
        a = (self.x_a[0] * n) + self.x_a[1]
        b = (self.x_b[0] * n) + self.x_b[1]

        # creates empty adjacency matrix
        matrix = np.zeros([pixels + 2, pixels + 2])
        for i1 in range(pixels):
            #connect all pixels to source node
            matrix[pixels][i1] = 442 - round(self.dist(I_list[i1],I_list[a]))
            #connect all pixels to sink node
            matrix[i1][pixels + 1] = 442 - round(self.dist(I_list[i1],I_list[b]))

            # creates a list of valid neighbor nodes using find_neighbors method
            neighbors = self.find_neighbors(n, i1)
            # assigns appropriate edge weights to valid neighbors
            for i2 in range(len(neighbors)):
                if (matrix[i1][neighbors[i2]] == 0):
                        matrix[i1][neighbors[i2]] = self.p0
                        matrix[neighbors[i2]][i1] = self.p0
        
        #returns the adjacency matrix
        return matrix
    
    # find_neighbors method that creates a list of nodes by unraveled index
    # that have dist < 2 with a given "index" node
    def find_neighbors(self, n, index):
        neighbors = []
        index_cord = [index // n, index % n]
        for i3 in range(-1,2):
            for i4 in range(-1,2):
                if (i3 != 0) or (i4 != 0):
                    if ((index_cord[0] + i3 >= 0) and ((index_cord[0] + i3 < n)) and
                        (index_cord[1] + i4 >= 0) and ((index_cord[1] + i4 < n))):
                        neighbors.append(index + (n * i3) + i4)
        return neighbors
    
    # Euclidian 3 dimensional vector distance calculator
    def dist(self, a, b):
        distances = [0,0,0]
        for i1 in range(3):
            distances[i1] = ((int(a[i1]) - int(b[i1])) ** 2)
        return (sum(distances) ** 0.5)
    
    # matrix_dfs that returns a path from the start node to the
    # goal node. If no path exists, the function returns all of the
    # nodes reachable from the start node
    def matrix_dfs(self, matrix, start, goal):
        visited = [start]
        path = [start]
        n = len(matrix)
        while start != goal:
            counter = 0
            found = False
            while counter < n:
                edge = matrix[start][counter]
                # this if statement can be changed to use a binary reduction,
                # but given that dimensions and hyperparameters are arbitrary,
                # we will not use that modification to Ford Fulkerson
                if (edge > 0) and (counter not in visited):
                    visited.append(counter)
                    path.append(counter)
                    start = counter
                    counter = n
                    found = True
                counter += 1
            if (start != goal) and (found == False):
                if (len(path) < 2):
                    return visited
                start = path[-2]
                path.pop()
        return path

    # ford_fulk method that creates a residual graph adjacency matrix
    # from a given graph and dfs path
    def ford_fulk(self, matrix, path):
        bottleneck = 500
        for i1 in range(len(path) - 1):
            if (matrix[path[i1]][path[i1 + 1]] < bottleneck):
                bottleneck = matrix[path[i1]][path[i1 + 1]]
        for i1 in range(len(path) - 1):
            matrix[path[i1]][path[i1 + 1]] -= bottleneck
            matrix[path[i1 + 1]][path[i1]] += bottleneck
        return matrix