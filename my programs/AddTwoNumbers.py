class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    @staticmethod
    def addTwoLists(num1: Node, num2: Node) -> Node:
        # Helper to push values onto stacks
        def build_stack(node):
            stack = []
            while node:
                stack.append(node.data)
                node = node.next
            return stack

        s1 = build_stack(num1)
        s2 = build_stack(num2)
        carry = 0
        result = None

        # Add values from stacks
        while s1 or s2 or carry:
            total = carry
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()

            carry, digit = divmod(total, 10)
            new_node = Node(digit)
            new_node.next = result
            result = new_node

        # Remove leading zeros if any
        while result and result.data == 0 and result.next:
            result = result.next

        return result
