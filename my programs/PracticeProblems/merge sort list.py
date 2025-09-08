class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def split(head):
    fast = head
    slow = head

    # Move fast pointer two steps and slow pointer
    # one step until fast reaches the end
    while fast and fast.next:
        fast = fast.next.next
        if fast:
            slow = slow.next

    # Split the list into two halves
    second = slow.next
    slow.next = None
    return second


def merge(first, second):
    # If either list is empty, return the other list
    if not first:
        return second
    if not second:
        return first

    # Pick the smaller value between first and second nodes
    if first.data < second.data:
        first.next = merge(first.next, second)
        return first
    else:
        second.next = merge(first, second.next)
        return second


def mergeSort(head):
    # Base case: if the list is empty or has only one node,
    # it's already sorted
    if not head or not head.next:
        return head

    # Split the list into two halves
    second = split(head)

    # Recursively sort each half
    head = mergeSort(head)
    second = mergeSort(second)

    # Merge the two sorted halves
    return merge(head, second)


def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        if curr.next:
            print("->", end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    # Create a hard-coded singly linked list:
    # 9 -> 8 -> 5 -> 2
    head = Node(9)
    head.next = Node(8)
    head.next.next = Node(5)
    head.next.next.next = Node(2)

    head = mergeSort(head)
    printList(head)