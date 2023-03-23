#percolation.py
#Jamison Talley

#This program is a python implementation of the classic
#percolation problem. This program can run as a stand
#alone demonstration of a percolation algorithm, or it
#could be used to create a probability analysis of the
#percolation threshold

import random

#creates a tree data type that allows us 
#to determine if there is a connection
#between two nodes
class tree:
    def __init__(self, n):
        self.container = []
        self.size = []
        for i1 in range(n):
            self.container.append(i1)
            self.size.append(1)

    def __str__(self):
        return str(self.container)
    
    def root(self, a):
        while self.container[a] != a:
            a = self.container[a]
        return a


    #uses a quick weighted union function that
    #merges smaller trees into larger ones to keep
    #tree hights at a minimum
    def q_w_union(self, a, b):
        c = self.root(a)
        d = self.root(b)
        if c == d:
            return
        if self.size[c] < self.size[d]:
            self.container[c] = d
            self.size[d] += self.size[c]
        else:
            self.container[d] = c
            self.size[c] += self.size[d]
        return

    #returns a boolean depending on if two nodes
    #are connected in the tree by comparing their roots
    def find(self, a, b):
        if self.root(a) == self.root(b):
            return True
        return False


#defines a function that creates an n x n grid where the
#probability of a space being open is equal to p
def make_grid(n, p):
    # p = open probability
    grid = []
    for i1 in range(n):
        grid.append([])
        for i2 in range(n):
            temp_rand = random.uniform(0,1)
            if temp_rand < p:
                grid[i1].append(0)
            else:
                grid[i1].append(1)
    return grid

#takes the grid created in the previous function and
#uses it to create a tree where nodes are connected
#if they are open and share adjacent spaces. We then
#see if the top is connected to the bottom by using two
#virtual nodes. We conneect the first virtual node (n*n)
#to each of the open nodes on the top of the grid, and we connect
#the second virtual node (n*n + 1) to each of the open nodes
#at the bottom of the grid
def make_tree(grid):
    n = len(grid)
    my_tree = tree((n * n) + 2)
    counter = 0
    for i1 in range(n):
        if grid[0][i1] == 0:
            my_tree.q_w_union(i1, n * n)
        counter += 1
    for i2 in range(1, n - 1):
        for i3 in range(n):
            if (grid[i2 - 1][i3] == 0) and (grid[i2][i3] == 0):
                my_tree.q_w_union(counter, counter - n)
            if ((i3 != n - 1) and (grid[i2][(i3 + 1) % n] == 0)
                                        and (grid[i2][i3] == 0)):
                my_tree.q_w_union(counter, counter + 1)
            counter += 1
    for i4 in range(n):
        if (grid[n - 2][i4] == 0) and (grid[n - 1][i4] == 0):
            my_tree.q_w_union(counter, counter - n)
        if grid[n - 1][i4] == 0:
            my_tree.q_w_union(counter, (n * n) + 1)
        counter += 1
    return my_tree

#defines a function to display the grid
def display_grid(grid):
    n = len(grid)
    for i1 in range(n):
        for i2 in range(n):
            if grid[i1][i2] == 0:
                print("  ", end="")
            else:
                print("██", end="")
        print()
    return

#defines a main function that obtains the grid size
#and open probability from the user, creates the grid,
#displays the grid, and outputs whether or not the grid
#will percolate
def main():
    p = 0.6
    n = 10
    cont_val = True
    
    #uses error handling to ensure valid user inputs
    while cont_val == True:
        print("enter the probability of a space being open:")
        user_input = input()
        try:
            p = float(user_input)
            cont_val = False
            if (p > 1) or (p < 0):
                print("invalid input...")
                cont_val = True
        except:
            print("invalid input...")
    cont_val = True
    while cont_val == True:
        print("enter the size of the grid: ")
        user_input = input()
        try:
            n = int(user_input)
            cont_val = False
            if n < 1:
                print("invalid input...")
                cont_val = True
        except:
            print("invalid input...")
    grid = make_grid(n, p)
    # grid = [[0,1,0,0],[1,1,0,1],[0,0,0,1],[1,0,1,0]]
    my_tree = make_tree(grid)
    display_grid(grid)
    print(my_tree.find(n * n, (n * n) + 1))
    # print(my_tree)

if __name__ == "__main__":
    main()