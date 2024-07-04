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
        if len(queue) == 0:
            return result

        current_node = queue.pop(0)
        result.append(current_node.value)

        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)

        return self.breadthFirstSearchRecursion(queue, result)
    
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(26)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.breadthFirstSearchRecursion([tree.root], []))
