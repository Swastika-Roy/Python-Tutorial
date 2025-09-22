def maxOfMin(arr):
    n = len(arr)
    res = [0] * n
    windowMax = [0] * (n + 1)
    st = []

    # Find previous and next smaller elements
    for i in range(n):
        while st and arr[st[-1]] >= arr[i]:
            top = st.pop()
            left = st[-1] if st else -1
            right = i
            wsize = right - left - 1
            windowMax[wsize] = max(windowMax[wsize], arr[top])
        st.append(i)

    # Process remaining elements in the stack
    while st:
        top = st.pop()
        left = st[-1] if st else -1
        right = n
        wsize = right - left - 1
        windowMax[wsize] = max(windowMax[wsize], arr[top])

    # Fill the result list
    for i in range(n):
        res[i] = windowMax[i + 1]

    # Ensure results are non-increasing
    for i in range(n - 2, -1, -1):
        res[i] = max(res[i], res[i + 1])

    return res


if __name__ == "__main__":
    arr = [10, 20, 30, 50, 10, 70, 30]
    result = maxOfMin(arr)
    print(" ".join(map(str, result)))