def sumSubMins(arr):
    n = len(arr)
    dp = [0] * n
    right = [i for i in range(n)]
    stack = []

    # Find index of next
    # smaller element on the right
    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            right[stack.pop()] = i
        stack.append(i)

    # Fill dp[] from right to left
    dp[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        r = right[i]
        if r == i:
            dp[i] = (n - i) * arr[i]
        else:
            dp[i] = (r - i) * arr[i] + dp[r]

    return sum(dp)


if __name__ == "__main__":
    arr = [3, 1, 2, 4]
    print(sumSubMins(arr))