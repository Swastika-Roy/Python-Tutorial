def build_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for value in arr[1:]:
        curr.next = Node(value)
        curr = curr.next
    return head

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print()

# Take user input
user_input = input("Enter 0s, 1s, and 2s separated by space: ")
arr = list(map(int, user_input.strip().split()))

# Build, segregate, and print linked list
head = build_linked_list(arr)
sorted_head = Solution.segregate(head)
print("Sorted linked list:")
print_linked_list(sorted_head)
