# Python program to find a pair with given sum in a Balanced BST
# Using Inorder Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to perform Inorder traversal and store the
# elements in an array
def inorderTraversal(root, inorder):
    if root is None:
        return

    inorderTraversal(root.left, inorder)

    # Store the current node's value
    inorder.append(root.data)

    inorderTraversal(root.right, inorder)


# Function to find if there exists a pair with a
# given sum in the BST
def findTarget(root, target):
    # Create an auxiliary array and store Inorder traversal
    inorder = []
    inorderTraversal(root, inorder)

    # Use two-pointer technique to find the pair with given sum
    left, right = 0, len(inorder) - 1

    while left < right:
        currentSum = inorder[left] + inorder[right]

        # If the pair is found, return true
        if currentSum == target:
            return True

        # If the current sum is less than the target,
        # move the left pointer
        if currentSum < target:
            left += 1

        # If the current sum is greater than
        # the target, move the right pointer
        else:
            right -= 1

    return False


if __name__ == "__main__":
    # BST structure
    #
    #        15
    #       /  \
    #     10   20
    #    / \   / \
    #   8  12 16 25

    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)

    target = 35

    print("True" if findTarget(root, target) else "False")
