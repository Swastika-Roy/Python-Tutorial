# Python program to correct the BST by replacing
# node values with sorted values

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


# Function to store the inorder
# traversal of the tree in an array
def findInorder(curr, inorder):
    if curr is None:
        return

    # Recursively store left subtree
    findInorder(curr.left, inorder)

    # Store the current node's data
    inorder.append(curr.data)

    # Recursively store right subtree
    findInorder(curr.right, inorder)


# Recursive function to correct the BST by replacing
# node values with sorted values
def correctBSTUtil(root, inorder, index):
    if root is None:
        return

    # Recursively fill the left subtree
    correctBSTUtil(root.left, inorder, index)

    # Replace the current node's data with
    # the correct value from the sorted array
    root.data = inorder[index[0]]
    index[0] += 1

    # Recursively fill the right subtree
    correctBSTUtil(root.right, inorder, index)

# Function to fix the given BST where two nodes are swapped.
def correctBST(root):
    # Array to store the inorder traversal of the tree
    inorder = []
    findInorder(root, inorder)

    # Sort the array to get the correct order of
    # elements in a BST
    inorder.sort()

    index = [0]
    correctBSTUtil(root, inorder, index)


# Print tree as level order
def printLevelOrder(root):
    if root is None:
        print("N", end=" ")
        return

    queue = [root]
    nonNull = 1

    while queue and nonNull > 0:
        curr = queue.pop(0)

        if curr is None:
            print("N", end=" ")
            continue
        nonNull -= 1

        print(curr.data, end=" ")
        queue.append(curr.left)
        queue.append(curr.right)
        if curr.left:
            nonNull += 1
        if curr.right:
            nonNull += 1


if __name__ == "__main__":
    # Constructing the tree with swapped nodes
    #       6
    #     /  \
    #    10   2
    #   / \  / \
    #  1  3 7  12
    # Here, 10 and 2 are swapped

    root = Node(6)
    root.left = Node(10)
    root.right = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.right = Node(12)
    root.right.left = Node(7)

    correctBST(root)
    printLevelOrder(root)
