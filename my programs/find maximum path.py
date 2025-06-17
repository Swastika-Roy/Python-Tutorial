# Python program to find maximum path sum in Binary Tree

class Node:
    # Constructor to initialize a new node
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


# Returns the maximum path sum in the subtree with the current node as an endpoint.
# Also updates 'res' with the maximum path sum.
def maxPathSumUtil(root, res):
    # Base case: return 0 for a null node
    if root is None:
        return 0

    # Calculate maximum path sums for left and right subtrees
    l = max(0, maxPathSumUtil(root.left, res))
    r = max(0, maxPathSumUtil(root.right, res))

    # Update 'res' with the maximum path sum passing through the current node
    res[0] = max(res[0], l + r + root.data)

    # Return the maximum path sum rooted at this node
    return root.data + max(l, r)


# Returns maximum path sum in tree with given root
def maxPathSum(root):
    res = [root.data]

    # Compute maximum path sum and store it in 'res'
    maxPathSumUtil(root, res)

    return res[0]


if __name__ == "__main__":
    # Representation of input binary tree:
    #            10
    #           /  \
    #          2    10
    #         / \     \
    #        20  1    -25
    #                 /  \
    #                3    4
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)

    print(maxPathSum(root))
