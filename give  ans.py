def longest_subarray(arr):
    n = len(arr)
    max_len = 0

    for l in range(n):
        max_in_sub = arr[l]
        for r in range(l, n):
            max_in_sub = max(max_in_sub, arr[r])
            length = r - l + 1
            if max_in_sub <= length:
                max_len = max(max_len, length)
    return max_len
