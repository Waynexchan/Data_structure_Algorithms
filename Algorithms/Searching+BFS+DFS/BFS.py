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
        currentNode = self.root
        result = []
        queue = []
        queue.append(currentNode) # append current node into the queue

        while(len(queue) > 0):
            currentNode = queue.pop(0)
            result.append(currentNode.value) # append current node value

            if currentNode.left is not None: #inset left handside into queue
                queue.append(currentNode.left)
            if currentNode.right is not None: #inset  right handside into queue
                queue.append(currentNode.right)

        return result
        
    
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(26)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.breadthFirstSearch())
