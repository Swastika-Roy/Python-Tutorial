# Python program to find the maximum of the minimums
# for every window size in the array

def maxOfMins(arr):
    n = len(arr)
    res = [0] * n
    s = []

    # Array to store the length of the window
    # where each element is the minimum
    lenArr = [0] * n

    # Traverse through array to determine
    # window sizes using a stack
    for i in range(n):

        # Process elements to find next smaller
        # element on the left
        while s and arr[s[-1]] >= arr[i]:
            top = s.pop()
            windowSize = i if not s else i - s[-1] - 1
            lenArr[top] = windowSize
        s.append(i)

    # Process remaining elements in the stack
    # for right boundaries
    while s:
        top = s.pop()
        windowSize = n if not s else n - s[-1] - 1
        lenArr[top] = windowSize

    # Fill res[] based on len_arr[] and arr[]
    for i in range(n):
        windowSize = lenArr[i] - 1  # 0-based indexing
        res[windowSize] = max(res[windowSize], arr[i])

    # Fill remaining entries in res[] to ensure
    # all are max of min
    for i in range(n - 2, -1, -1):
        res[i] = max(res[i], res[i + 1])

    return res


if __name__ == '__main__':
    arr = [10, 20, 30, 50, 10, 70, 30]
    res = maxOfMins(arr)
    print(' '.join(map(str, res)))