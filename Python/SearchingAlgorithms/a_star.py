#a_star.py
#Jamison Talley
#24-2-23

from fast_linked_list import linked_list
from fast_linked_list import node
    

def ordered_insert(user_list: linked_list, new_val:list):
    #this function will take a linked list where each data value
    #is a list with a value and a 'rank'. The 'rank' will 
    #be used to sort the values. Note this funciton only works if you are
    #inserting a value into an already sorted linked list.

    if user_list.len > 1:
        prev_node = user_list.head
        current = user_list.head.next
        while current != None:
            if current.data[1] > new_val[1]:
                new_node = node(new_val, current)
                prev_node.next = new_node
                i1 = user_list.len
                user_list.len += 1
                return user_list
            else:
                prev_node = prev_node.next
                current = current.next
    user_list.append(new_val)
    return user_list

#this is an implementation of the a star aglorithm
#that takes a matrix graph as input. This algorithm
#works by creating an ordered queue of nodes to explore.
#Instead of using a standard enqueue function, we use the
#above 'ordered_insert' function. The afformentioned 'rank'
#is determined by the heuristic value of the node (h(n)) and
#the path cost to get to that node (g(n)). Thus:
#rank = h(n) + g(n)
def matrix_a_star(matrix, potentials, start, goal):
    n = len(matrix)
    current = start
    path = linked_list()
    parents = [i for i in range(n)]
    node_cost = [0 for i in range(n)]
    opened = [False for i in range(n)]
    queue = linked_list([start, 0, start, 0])
    while (current != goal):
        current = queue.head.data[0]
        if (opened[current] == False):
            parents[current] = queue.head.data[2]
            node_cost[current] = queue.head.data[3]
            opened[current] = True
            for i1 in range(n):
                edge = matrix[current][i1]
                if (edge > 0) and (opened[i1] == False):
                    queue = ordered_insert(queue, [i1,
                            node_cost[current] + edge + potentials[i1],
                            current, node_cost[current] + edge])
        queue.pop()
    cur = goal
    while cur != start:
        path.push(cur)
        cur = parents[cur]
    path.push(start)
    out_list = []
    for i2 in range(len(path)):
        out_list.append(path.pop())
    return out_list

#creates a test client for the algorithm
def main():
    n = 8
    matrix_graph = [[0] * n for i1 in range(n)]
    matrix_graph[0][1] = 1
    matrix_graph[0][2] = 2
    matrix_graph[1][3] = 1
    matrix_graph[1][4] = 1
    matrix_graph[2][5] = 3
    matrix_graph[4][7] = 1
    matrix_graph[4][6] = 1
    matrix_graph[6][5] = 1
    matrix_graph[7][6] = 1
    potentials = [4, 3, 3.1, 4, 2, 0, 2, 2]
    for i2 in range(n):
        print(matrix_graph[i2])
    print()
    print(matrix_a_star(matrix_graph, potentials, 0, 5))
    return

if __name__ == "__main__":
    main()