class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverseList(self, head):
        stack = []
        temp = head

        # Push all nodes into stack
        while temp:
            stack.append(temp)
            temp = temp.next

        # If stack is not empty, set new head
        if stack:
            head = stack.pop()
            temp = head

            # Pop all remaining nodes and link them
            while stack:
                temp.next = stack.pop()
                temp = temp.next

            # Set next of last node to None
            temp.next = None

        return head
