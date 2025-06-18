# Python Program to Count all K Sum Paths in Binary Tree
# By Exploring All Possible Paths

class Node:
    def __init__(self, k):
        self.data = k
        self.left = None
        self.right = None


# Function to count paths with sum k starting from the given node
def countPathsFromNode(node, k, currentSum):
    if node is None:
        return 0

    pathCount = 0

    # Update the current sum
    currentSum += node.data

    # If current sum equals k, increment path count
    if currentSum == k:
        pathCount += 1

    # Recur for the left and right subtree
    pathCount += countPathsFromNode(node.left, k, currentSum)
    pathCount += countPathsFromNode(node.right, k, currentSum)

    return pathCount


# Function to count all paths that sum to k in the binary tree
def countAllPaths(root, k):
    if root is None:
        return 0

    # Count all paths starting from the current node
    res = countPathsFromNode(root, k, 0)

    # Recur for the left and right subtree
    res += countAllPaths(root.left, k)
    res += countAllPaths(root.right, k)

    return res


if __name__ == "__main__":
    # Create a sample tree:
    #        8
    #      /  \
    #     4    5
    #    / \    \
    #   3   2    2
    #  / \   \
    # 3  -2   1

    root = Node(8)
    root.left = Node(4)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right.right = Node(2)
    root.left.left.left = Node(3)
    root.left.left.right = Node(-2)
    root.left.right.right = Node(1)

    k = 7
    print(countAllPaths(root, k))
