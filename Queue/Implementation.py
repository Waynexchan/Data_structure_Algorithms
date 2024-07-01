class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.first is None:
            return None
        return self.first.data
        
    def enqueue(self, data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        
    def dequeue(self):
        if self.first is None:
            return None
        dequeued_node = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.length -= 1
        return dequeued_node.data
    
    def print_queue(self):
        if self.length == 0:
            print("Queue Empty")
            return
        else:
            current_pointer = self.first
            while(current_pointer != None):
                if current_pointer.next ==None:
                    print(current_pointer.data)
                else:
                    print(f'{current_pointer.data}  <<--  ', end='')
                current_pointer = current_pointer.next
            return
        