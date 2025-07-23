def subarraySum(arr):
    n = len(arr)
    result = 0

    # pick starting point
    for i in range(n):
        temp = 0

        # pick ending point
        for j in range(i, n):
            # sum subarray between current starting
            # and ending points
            temp += arr[j]
            result += temp
    return result


if __name__ == "__main__":
    arr = [1, 4, 5, 3, 2]
    print(subarraySum(arr))