def modified_binary_search(arr, target):
    l, r = 0, len(arr) - 1

    while r >= l:
        mid = l + (r - l) // 2

        # Check the middle 3 positions
        if arr[mid] == target:
            return mid
        if mid > l and arr[mid - 1] == target:
            return mid - 1
        if mid < r and arr[mid + 1] == target:
            return mid + 1

        # Search in left subarray
        if arr[mid] > target:
            r = mid - 2
        else:
            l = mid + 2

    # Element not found
    return -1
