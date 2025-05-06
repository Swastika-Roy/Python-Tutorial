def requiredindex(arr):
    second_max = -1
    first_max = -1
    max_idx = 0
    for i in range(len(arr)):
        if arr[i] > first_max:
            second_max = first_max
            first_max = arr[i]
            max_idx = i
        elif arr[i] > second_max:
            second_max = arr[i]
    return max_idx

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
idx = requiredindex(arr)
print("Index of largest element:", idx)
