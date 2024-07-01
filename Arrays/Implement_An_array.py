class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)
    
    def get(self, index):
        return self.data[index] #O(1)
    
    def push(self, item):
        self.length += 1 
        self.data[self.length-1] = item # O(1)

    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item #O(1)
    
    def insert(self, index, item):
        self.length += 1
        for i in range(self.length-1, index, -1):
            self.data[i] =self.data[i-1]
            self.data[index] = item # O(n)

    def delete(self, index):
        for i in range (index, self.length-1):
            self.data[i] = self.data[i+1]
            del self.data [self.length-1]
            self.length -= 1 #O(n)