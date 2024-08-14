#fast_linked_list.py
#Jamison Talley
#18-2-23

#creates a node data type of which the linked
#list data type is built
class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return str([self.data, self.next])

#this is an implementation of a singly linked list
#that keeps track of the tail of the list, as well
#as the head of the list in the class data. This allows
#both push and enqueue style functions to be completed
#in constant time. 
class linked_list:
    def __init__(self, head=None):
        self.head = node(head, None)
        self.tail = self.head
        self.len = 1
        if head == None:
            self.len = 0

    def __len__(self):
        return self.len

    #defines a method that adds a value at the
    #end of the list
    def append(self, data):
        if self.head == None:
            self.head = node(data)
            self.tail = self.head
            self.len = 1
            return
        elif self.head.data == None:
            self.head = node(data)
            self.tail = self.head
            self.len = 1
            return
        else:
            self.tail.next = node(data, None)
            self.tail = self.tail.next
            self.len += 1
        return

    #defines a method that adds a value at the beginning
    #of the list
    def push(self, data):
        if self.len == 0:
            self.head = node(data, None)
            self.tail = self.head
        else:
            new_node = node(data, self.head)
            self.head = new_node
            self.tail = self.head
        self.len += 1
        return

    #defines a method that returns the value of any
    #location in the list as long as the specified
    #index is valid
    def get(self, depth=0):
        if (depth >= self.len) or (depth < 0):
            return None
        current = self.head
        for i1 in range(depth):
            current = current.next
        return current.data

    #defines a method that deletes a value from the list
    #and returns it. By default, this is the first head of
    #the linked list, but the method also allows for the
    #removal of any index of the list.
    def pop(self, depth=0):
        if (depth >= self.len) or (depth < 0):
            return False
        elif depth == 0:
            val = self.head.data
            self.head = self.head.next
            self.len -= 1
            return val
        current = self.head
        prev_node = None
        for i1 in range(depth):
            prev_node = current
            current = current.next
        val = current.data
        prev_node.next = current.next
        self.len -= 1
        return val
    
    #establishes an __str__ method
    def __str__(self):
        current = self.head
        string = str(current.data) + "  "
        while current.next != None:
            current = current.next
            string += str(current.data) + "  "
        return string
        

#creates a test client for the data type
def main():
    my_list = linked_list()
    my_list.append('a')
    my_list.push('b')
    my_list.pop()
    print(my_list)


if __name__ == "__main__":
    main()