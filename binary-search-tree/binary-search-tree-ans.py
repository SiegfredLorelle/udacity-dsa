class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Start with the root
        current = self.root
        # Loop until the proper location of the new node is found 
        while True:
            # If curernt value is less then given value, then it should be in the left
            if current.value > new_val:
                # If there is a node in the left, then go to that node
                if current.left:
                    current = current.left
                # If no node, then that position is perfect for the new node
                else:
                    current.left = Node(new_val)
                    break
            # if current value is greater than given value, then it should be in the right
            elif current.value < new_val:
                # If there is a node in the right, then go to that node
                if current.right:
                    current = current.right
                # If no node, then that position is perfect for the new node
                else:
                    current.right = Node(new_val)
                    break
            # Catches error, incase user tried to enter a repeat value
            elif current.value == new_val:
                print("ERROR: number already in binary tree")

    def search(self, find_val):
        # Start with the root
        current = self.root
        # Loop until the the given value is found, or that it is not found in its appropriate location
        while True:
            # It is found, if current value is same as given value 
            if current.value == find_val:
                return True
            # If current value is greater than given value, then go to left node if it exists
            elif current.value > find_val and current.left:
                current = current.left
            # If courrent value is less than given value, then go to the right node if it exists
            elif current.value < find_val and current.right:
                current = current.right
            # If not found in its appropriate location then it does not exist
            else:
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