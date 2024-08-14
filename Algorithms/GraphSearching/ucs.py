#ucs.py
#Jamison Talley
#24-2-23

from fast_linked_list import linked_list
from fast_linked_list import node

def ordered_insert(user_list: linked_list, new_val:list):
    #this function will take a linked list where each data value
    #is a list with a value and a 'rank'. The 'rank' will be used
    #to sort the values. Note this funciton only works if you are
    #inserting a value into an already sorted linked list.
    
    if new_val[1] < user_list.head.data[1]:
        new_node = node(new_val,user_list.head)
        user_list.head = new_node
        user_list.len += 1
        return user_list
    elif user_list.len > 1:
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

#this is an implementation of the uniform cost search aglorithm
#that takes a matrix graph as input. This algorithm
#works by creating an ordered queue of nodes to explore.
#Instead of using a standard enqueue function, we use the
#above 'ordered_insert' function. The afformentioned 'rank'
#is determined by path cost to get to a specific node (g(n))
def matrix_ucs(matrix, start, goal):
    n = len(matrix)
    current = start
    path = linked_list()
    parents = [i for i in range(n)]
    node_cost = [0 for i in range(n)]
    opened = [False for i in range(n)]
    queue = linked_list([start, 0, start])
    while (current != goal):
        current = queue.head.data[0]
        if (opened[current] == False):
            parents[current] = queue.head.data[2]
            node_cost[current] = queue.head.data[1]
            opened[current] = True
            for i1 in range(n):
                edge = matrix[current][i1]
                if (edge > 0) and (opened[i1] == False):
                    queue = ordered_insert(queue, [i1, node_cost[current] + edge, current])
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

#defines a test client for the ordered_insert function
def ordered_insert_test():
    my_list = linked_list([0,0])
    my_list = ordered_insert(my_list, [1,1])
    my_list = ordered_insert(my_list, [2,2])
    my_list = ordered_insert(my_list, [3,14])
    my_list = ordered_insert(my_list, [3,18])
    my_list = ordered_insert(my_list, [4,4])
    my_list = ordered_insert(my_list, [4,17])
    my_list = ordered_insert(my_list, [-1,-1])
    my_list = ordered_insert(my_list, [-1,15])
    print(my_list)
    return

#defines a test client for the matrix_ucs function
def main():
    n = 7
    matrix_graph = [[0] * n for i1 in range(n)]
    matrix_graph[0][1] = 1
    matrix_graph[0][2] = 2
    matrix_graph[1][3] = 1
    matrix_graph[1][4] = 1
    matrix_graph[2][5] = 3
    matrix_graph[4][5] = 5
    matrix_graph[4][6] = 1
    matrix_graph[6][5] = 1
    for i2 in range(n):
        print(matrix_graph[i2])
    print()
    print(matrix_ucs(matrix_graph, 0, 5))
    return

if __name__ == "__main__":
    main()