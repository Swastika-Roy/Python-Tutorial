from collections import defaultdict


def find_majority_element():
    # Get user input for the array
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

    n = len(arr)
    count_map = defaultdict(int)

    for num in arr:
        count_map[num] += 1

        # Check if current element count exceeds n / 2
        if count_map[num] > n // 2:
            return num

    # If no majority element is found
    return -1


# Call the function and print the result
result = find_majority_element()
print("Majority element:", result)