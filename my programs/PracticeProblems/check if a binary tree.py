# Python program to check if a tree is BST using Morris Traversal

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


# Function to check if the binary tree is a
# BST using Morris Traversal
def isBST(root):
    curr = root
    prevValue = float('-inf')

    while curr:
        if curr.left is None:

            # Process curr node
            if curr.data <= prevValue:
                # Not in ascending order
                return False
            prevValue = curr.data
            curr = curr.right
        else:

            # Find the inorder predecessor of curr
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right

            if pre.right is None:

                # Create a temporary thread to the curr node
                pre.right = curr
                curr = curr.left
            else:

                # Remove the temporary thread
                pre.right = None

                # Process the curr node
                if curr.data <= prevValue:
                    # Not in ascending order
                    return False
                prevValue = curr.data
                curr = curr.right

    return True


if __name__ == "__main__":

    # Create a sample binary tree
    #     10
    #    /  \
    #   5    20
    #        / \
    #       9   25

    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.right.left = Node(9)
    root.right.right = Node(25)

    if isBST(root):
        print("True")
    else:
        print("False")

