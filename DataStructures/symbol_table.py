#symbol_table.py
#Jamison Talley
#14-2-23

#this program is a basic implementation of a symbol table
#data structure from scratch. This is not meant to replace
#python dictionaries, but rather to demonstrate how they work.
#note: this program does not handle array resizing

class symbol_table:
    def __init__(self, size=32, input_array=[]):
        self.size = size
        self.array = [[] for i1 in range(size)]
        for i2 in range(len(input_array)):
            self.add_value(input_array[i2][0], input_array[i2][1])
    
    def get_hash(self, key):
        key_hash = 0
        for char in key:
            key_hash += ord(char)
        key_hash %= self.size
        return key_hash

    def add_value(self, key, value):
        hash = self.get_hash(key)
        for i1 in range(len(self.array[hash])):
            if (self.array[hash][0] != key):
                self.array[hash].append([key, value])
                return
        self.array[hash].append([key, value])
        return

    def get_val(self, key):
        hash = self.get_hash(key)
        bucket = self.array[hash]
        for i1 in range(len(bucket)):
            if bucket[i1][0] == key:
                return bucket[i1][1]
        # print("error, no key-value pair found...")
        return None

    def pop_val(self, key):
        hash = self.get_hash(key)
        bucket = self.array[hash]
        for i1 in range(len(bucket)):
            if bucket[i1][0] == key:
                val = bucket[i1][1]
                bucket.pop(i1)
                return val
        # print("error, no key-value pair found...")
        return None

    def __str__(self):
        return str(self.array)

def main():
    my_dict = symbol_table(32)
    my_dict.add_value("a", 10)
    my_dict.add_value("b", 20)
    print(my_dict.get_val("a"))
    print(my_dict.pop_val("b"))
    print(my_dict)


if __name__ == "__main__":
    main()