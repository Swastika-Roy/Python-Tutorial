class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None


def reverse(head):
    # If the list is empty or has only one node,
    # return the head as is
    if head is None or head.next is None:
        return head

    prevNode = None
    currNode = head

    # Traverse the list and reverse the links
    while currNode is not None:
        # Swap the next and prev pointers
        prevNode = currNode.prev
        currNode.prev = currNode.next
        currNode.next = prevNode

        # Move to the next node in the original list
        # (which is now previous due to reversal)
        currNode = currNode.prev

    return prevNode.prev


def printList(node):
    while node is not None:
        print(node.data, end="")
        if node.next is not None:
            print(" <-> ", end="")
        node = node.next
    print()


