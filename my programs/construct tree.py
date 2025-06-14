# Python program to construct tree using
# inorder and preorder traversals

from collections import deque


class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


# Print tree as level order
def printLevelOrder(root):
    if root is None:
        print("N ", end="")
        return

    qq = deque([root])
    nonNull = 1

    while qq and nonNull > 0:
        curr = qq.popleft()

        if curr is None:
            print("N ", end="")
            continue
        nonNull -= 1

        print(curr.data, end=" ")
        qq.append(curr.left)
        qq.append(curr.right)
        if curr.left:
            nonNull += 1
        if curr.right:
            nonNull += 1


# Recursive function to build the binary tree.
def buildTreeRecur(mp, preorder, preIndex, left, right):
    # For empty inorder array, return None
    if left > right:
        return None

    rootVal = preorder[preIndex[0]]
    preIndex[0] += 1

    # create the root Node
    root = Node(rootVal)

    # find the index of Root element in the in-order array.
    index = mp[rootVal]

    # Recursively create the left and right subtree.
    root.left = buildTreeRecur(mp, preorder, preIndex, left, index - 1)
    root.right = buildTreeRecur(mp, preorder, preIndex, index + 1, right)

    return root


# Function to construct tree from its inorder and preorder traversals
def buildTree(inorder, preorder):
    # Hash map that stores index of a root element in inorder array
    mp = {value: idx for idx, value in enumerate(inorder)}
    preIndex = [0]

    return buildTreeRecur(mp, preorder, preIndex, 0, len(inorder) - 1)


if __name__ == "__main__":
    inorder = [3, 1, 4, 0, 5, 2]
    preorder = [0, 1, 3, 4, 2, 5]
    root = buildTree(inorder, preorder)

    printLevelOrder(root)
