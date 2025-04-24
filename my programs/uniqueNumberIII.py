def get_single(arr):
    freq = {}

    # Count frequency of each element
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Return the element that appears only once
    for num, count in freq.items():
        if count == 1:
            return num

    return 0

# User input handling
arr = list(map(int, input("Enter elements separated by space: ").split()))
result = get_single(arr)
print("Element that appears only once:", result)
