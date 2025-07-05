def maxSum(arr):
    n = len(arr)

    # find two consecutive elements with maximum sum
    res = arr[0] + arr[1]
    for i in range(1, n - 1):
        res = max(res, arr[i] + arr[i + 1])

    return res

if __name__ == "__main__":
    arr = [5, 4, 3, 1, 6]
    print(maxSum(arr))