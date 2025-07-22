# Python program to find the minimum number
# of jumps to reach the end of the array

def minJumps(arr):
    n = len(arr)

    # array to memoize values
    dp = [float('inf')] * n
    dp[n - 1] = 0

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, min(i + arr[i] + 1, n)):
            if dp[j] != float('inf'):
                dp[i] = min(dp[i], 1 + dp[j])

    # If end cannot be reached.
    if dp[0] == float('inf'):
        return -1

    return dp[0]

if __name__ == "__main__":
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print(minJumps(arr))