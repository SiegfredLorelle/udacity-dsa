class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        is_found = self.preorder_search(self.root, find_val)
        return is_found

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal_sequence = self.preorder_print(self.root, str(self.root.value))
        return traversal_sequence

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        current = start
        if current.value == find_val:
            return True
        else:
            if current.left:
                is_found = self.preorder_search(current.left, find_val)
                if is_found:
                    return is_found
            if current.right:
                is_found = self.preorder_search(current.right, find_val)
                if is_found:
                    return is_found
                return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        current = start
        # print(traversal + str(1) + str(3))
        if current.left:
            traversal = self.preorder_print(current.left, traversal + "-" + str(current.left.value))
        if current.right:
            traversal = self.preorder_print(current.right, traversal + "-" + str(current.right.value))
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())