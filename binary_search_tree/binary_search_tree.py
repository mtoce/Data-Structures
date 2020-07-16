"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value < Node's value
        if value < self.value:
            # we need to go left 
            # if we see that there is no left child, 
            if self.left is None:
                # then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child 
            else:
                # call the left child's `insert` method 
                self.left.insert(value)
        # otherwise, value >= Node's value 
        else:
            # we need to go right 
            # if we see there is no right child, 
            if self.right is None:
                # then we can wrap the value in a BSTNode and park it 
                self.right = BSTNode(value)
            # otherwise there is a child 
            else:
                # call the right child's `insert` method 
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Instantiate the target value you're looking for
        value = target
        # If the instantiated value is the root node return it
        if value == self.value:
            return True
        # If the instantiated value is less than the root node
        elif value < self.value:
            # And there are child nodes to the left 
            if self.left is not None:
                # Check them and return True/False based on if the value matches the target
                return self.left.contains(value)
        # If the instantiated value is less than the root node
        elif value >= self.value:
            # And there are child nodes to the right
            if self.right is not None:
                # Check them and return True/False based on if the value matches the target
                return self.right.contains(value)

    # Return the maximum value found in the tree
    def get_max(self):
        # If there are no child nodes to the right of the root
        if self.right is None:
            # Return the value of the root node
            return self.value
        # If there are children nodes to the right
        else:
            # Check them until the maximum value is found
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Call fn function on the root node
        fn(self.value)
        # If there are nodes to the left of the root
        if self.left is not None:
            # Apply fn function to each node to the left
            self.left.for_each(fn)
        # If there are nodes to the right of the root
        if self.right is not None:
            # Apply fn function to each node to the left
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # Lowest number is always furthest to the left
        # base case 
        if node is None:
            return
        else:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
