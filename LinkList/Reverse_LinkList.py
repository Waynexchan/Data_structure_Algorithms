# 10-->5-->16

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node =Node(data)
        if self.head == None:

            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length +=1
        else:
            new_node.next =self.head
            self.head = new_node
            self.length += 1

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end= " ")
                current_node = current_node.next
        print()

    def insert(self, position, data):
        if position >= self.length:
            if position > self.length:
                print("This position is not available. Inserting at the end of the list")
            
            new_node = Node(data)
            self.tail.next = new_node
            self.tail =new_node
            self.length +=1

        elif position == 0:
            new_node =Node(data)
            self.tail.next = self.head
            self.head = new_node
            self.length +=1
        
        else:
            new_node = Node(data)
            current_node =self.head
            for i in range(position-1):
                current_node=current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length +=1

    def delete_by_value(self, data):
        if self.head ==None:
            print("Linked List is empty. Nothing to delete.")
            return
        current_node = self.head

        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next ==None:
                self.tail = self.head
            self.length -= 1
            return
        
        while current_node.next!= None and current_node.next.data != data:
            current_node=current_node.next
        
        if current_node.next != None:
            current_node.next=current_node.next.next
            if current_node.next ==None:
                self.tail = current_node
            self.length -=1
            return
        else:
            print("Given value not found.")

    def delete_by_position(self, position):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        if position>=self.length:
            position = self.length-1
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return
    

my_linked_list = LinkList()


def reverse(linked_list):
    if linked_list.length <=1:
        return linked_list
    else:
        first = linked_list.head
        second = first.next
        linked_list.tail = linked_list.head
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        linked_list.head.next = None
        linked_list.head = first
        return linked_list