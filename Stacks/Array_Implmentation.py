class Stack():
    def __init__(self):
        self.array = []

    def peak(self):
        return self.array[len(self.array)-1]
    
    def push(self, data):
        self.array.append(data)
        return
    
    def pop(self):
        if len(self.array) == 0:
            print("Empty Stack")
            return
        else:
            self.array.pop()
            return
        
    def print_stack(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i])
        return