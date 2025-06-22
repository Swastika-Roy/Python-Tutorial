# Python program to find kth
# smallest value in BST

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


# Recursive function for inorder traversal of the tree
# and find its kth smallest value.
# Returns -1 if value is not found.
def kthSmallestRecur(root, cnt, k):
    if root is None:
        return -1

    # Process left subtree.
    left = kthSmallestRecur(root.left, cnt, k)

    # If kth smallest is found in left
    # subtree, then return it.
    if left != -1:
        return left

    # increment node count
    cnt[0] += 1

    # If curr node is kth smallest,
    # return it.
    if cnt[0] == k:
        return root.data

    # Else process the right subtree
    # and return its value.
    right = kthSmallestRecur(root.right, cnt, k)
    return right


# Function to find kth smallest value in BST.
def kthSmallest(root, k):
    cnt = [0]
    return kthSmallestRecur(root, cnt, k)


if __name__ == "__main__":
    # Binary search tree
    #      20
    #    /   \
    #   8     22
    #  / \
    # 4   12
    #    /  \
    #   10   14
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    k = 3

    print(kthSmallest(root, k))
