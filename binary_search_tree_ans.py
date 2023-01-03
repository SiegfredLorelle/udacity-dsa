class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__ (self):
        return f"{self.value}"

class BST(object):
    def __init__(self, root):
        self.root = Node(root)


    def insert(self, new_val):
        current = self.root
        while new_val < current.value:
            if current.left:
                current = current.left
            else:
                current.left = Node(new_val)
                break
            
        while new_val > current.value:
            if current.right:
                current = current.right
            else:
                current.right = Node(new_val)
                break
                
        print(current.value, current.left, current.right)

    def search(self, find_val):
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))