#array_queue.py
#21-2-23
#Jamison Talley

#this program is a proof of concept implementation of an
#array queue
class array_queue:
    def __init__(self):
        self.array = [None for i in range(10)]
        self.locs = [0,0]

    def pop(self):
        val = self.array[self.locs[0]]
        if val == None:
            return IndexError
        self.array[self.locs[0]] = None
        self.locs[0] = (self.locs[0] + 1) % len(self.array)
        return val

    def enqueue(self, val):
        self.array[self.locs[1]] = val
        self.locs[1] = (self.locs[1] + 1) % len(self.array)
        return
    
    def __str__(self) -> str:
        return str(self.array)