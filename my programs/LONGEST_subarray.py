def longestSubarray(arr, k):
    n = len(arr)
    mp = {}
    ans = 0
    sum = 0

    for i in range(n):
        # Treat elements <= k as -1, > k as +1
        if arr[i] <= k:
            sum -= 1
        else:
            sum += 1

        # If sum is positive, prefix is valid
        if sum > 0:
            ans = i + 1
        else:
            # Check if prefix sum sum-1 occurred before
            if (sum - 1) in mp:
                ans = max(ans, i - mp[sum - 1])

        # Store first occurrence of this sum
        if sum not in mp:
            mp[sum] = i

    return ans

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 1]
    k = 2
    print(longestSubarray(arr, k))