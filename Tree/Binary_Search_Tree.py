class Node():
    def __init__(self):
        self.left = None
        self.right=None
        self.value = ValueError

class BinarySearchTree():
    def __init__(self):
        self.root=None
        self.number_of_nodes = 0

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            self.number_of_nodes += 1
            return
        
        else:
            current_node = self.root
            while(current_node.left != new_node) and (current_node.right != new_node):
                # right
                if new_node.data >current_node.data:
                    if current_node.right == None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                #left
                elif new_node.data < current_node.data:
                    if current_node.left == None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
            
            self.number_of_nodes +=1
            return
        
    def search(self,data):
        if self.root == None:
            return "Tree is empty"
        else:
            current_node = self.root
            while (current_node):
                if current_node ==None:
                    return "Not Found"
                if current_node.data == data:
                    return "Found"
                elif current_node.data > data:
                    current_node = current_node.left
                elif current_node.data < data:
                    current_node = current_node.right

    def remove(self, data):
        if self.root == None:
            return "Tree is Empty"
        current_node = self.root
        parent_node = None
        while current_node != None:
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left
            elif current_node < data:
                parent_node = current_node
                current_node = current_node.right
            else:#Match is found. Different cases to be checked
                #Node has left child only
                if current_node.right ==None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return
                #Node has right child only        
                elif current_node.left ==None:
                    if parent_node ==None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return
                        
                #Node has neither left nor right child
                elif current_node.left == None and current_node.right == None:
                    if parent_node == None:
                        current_node = None
                        return
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                        return
                    

                #Node has both left and right child
                elif current_node.left != None and current_node.right !=None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left != None:
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.data = del_node.data
                    if del_node == del_node_parent:
                        current_node.right = del_node.right
                        return
                    if del_node.right ==None:
                        del_node_parent.left =None
                        return
                    else:
                        del_node_parent.left = del_node.right
                        return
                    
            return "Not Found"
                        
                    