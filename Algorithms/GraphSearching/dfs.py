#matrix_dfs.py
#Jamison Talley
#16-2-23


#this is a recursive implementation of the depth first search algorithm
#that takes a matrix graph as input.
def matrix_dfs(matrix, start, goal, visited=[], path=[]):
    n = len(matrix)
    counter = 0
    if visited == []:
        visited = [start]
        path = [start]
    if start == goal:
        return path
    while counter < n:
        edge = matrix[start][counter]
        if (edge == 1) and (counter not in visited):
            visited.append(counter)
            path.append(counter)
            return matrix_dfs(matrix, counter, goal, visited, path)
        counter += 1
    path.pop()
    return matrix_dfs(matrix, path[-1], goal, visited, path)

#this is a dynamic implementation of the depth first search algorithm
#that takes a matrix graph as iput
def dynamic_matrix_dfs(matrix, start, goal, visited=[], path=[]):
    n = len(matrix)
    if visited == []:
        visited = [start]
        path = [start]
    while start != goal:
        counter = 0
        found = False
        while counter < n:
            edge = matrix[start][counter]
            if (edge > 0) and (counter not in visited):
                visited.append(counter)
                path.append(counter)
                start = counter
                counter = n
                found = True
            counter += 1
        if (start != goal) and (found == False):
            start = path[-2]
            path.pop()
    return path

#creates a main function to test the above functions
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
    print(matrix_dfs(matrix_graph, 3, 5))
    print(dynamic_matrix_dfs(matrix_graph, 3, 4))
    return

if __name__ == "__main__":
    main()