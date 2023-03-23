#bfs.py
#21-2-23
#Jamison Talley

from fast_linked_list import linked_list

#this is an implementation of the breadth first search algorithm
#that takes a matrix graph as input. This implementation uses a
#linked list as a queue to store the order of nodes to explore.
def matrix_bfs(matrix, start, goal):
    n = len(matrix)
    parent_matrix = [[0 for i in range(n)] for j in range(n)]
    visited = [start]
    queue = linked_list(start)
    level = 0
    current = None
    cont = True
    while cont == True:
        nodes = len(queue)
        for i1 in range(nodes):
            current = queue.get()
            queue.pop()
            if current == goal:
                cont = False
            for i2 in range(n):
                if ((matrix[current][i2] > 0) and (i2 not in visited)
                    and (current != goal)):
                    parent_matrix[i2][current] = 1
                    queue.append(i2)
                    visited.append(i2)
        level += 1
    path = [0 for i in range(level)]
    parent = goal
    for i3 in range(level):
        node = parent
        path[(level - i3 - 1)] = node
        i4 = 0
        while i4 < n:
            if parent_matrix[node][i4] > 0:
                parent = i4
                i4 = n
            i4 += 1
    return path


#defines a main function to test the implementation
def main():
    n = 6
    node_names = ['2','3','4','5','7','8']
    matrix_graph = [[0] * n for i1 in range(n)]
    matrix_graph[3][1] = 1
    matrix_graph[3][4] = 1
    matrix_graph[1][0] = 1
    matrix_graph[1][2] = 1
    matrix_graph[2][5] = 1
    matrix_graph[4][5] = 1
    for i2 in range(n):
        print(matrix_graph[i2])
    print(matrix_bfs(matrix_graph, 1, 5))
    return

if __name__ == "__main__":
    main()
