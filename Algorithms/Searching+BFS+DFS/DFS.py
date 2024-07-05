class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    current_node = current_node.right

    def lookup(value):
        pass

    def remove(value):
        pass

    def breadthFirstSearch(self):
        pass

    def breadthFirstSearchRecursion(self, queue, result):
        pass

    def DFSInOrder(self):
        return self.traverseInOrder(self.root, [])

    def DFSPostOrder(self):
        return self.traversePostOrder(self.root, [])
    
    def DFSPreOrder(self):
        return self.traversePreOrder(self.root, [])
    
    def traverseInOrder(self, node, result):
        if node.left:
            self.traverseInOrder(node.left, result)
        result.append(node.value)
        if node.right:
            self.traverseInOrder(node.right, result)
        return result
    
    def traversePostOrder(self, node, result):
        

        if node.left:
            self.traversePostOrder(node.left, result)
           
        if node.right:
            self.traversePostOrder(node.right, result)
        result.append(node.value)
        return result
    
    def traversePreOrder(self, node, result):
        result.append(node.value)

        if node.left:
            self.traversePreOrder(node.left, result)
        if node.right:
            self.traversePreOrder(node.right, result)
        return result
    
    #O (height of tree)
    
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# print(tree.breadthFirstSearchRecursion([tree.root], []))
print(tree.DFSPostOrder())