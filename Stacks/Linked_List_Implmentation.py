class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top == None:
            return None
        else:
            return self.top.data
        
    def push(self, data):
        new_node = Node(data):
        if self.top ==None:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1 

    def pop(self, data):
        
        if self.top == None:
            print ("Empty")
        else:
            self.top = self.top.next
            self.length -= 1
            if (self.length ==0):
                self.bottom = None

    def print_stack(self):
        if self.top == None:
            print ("Empty")
        else:
            current_pointer = self.top
            while (current_pointer!= None):
                print(current_pointer.data)
                current_pointer= current_pointer.next