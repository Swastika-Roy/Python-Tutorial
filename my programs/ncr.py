def nCr(n, k):
    dp = [0] * (k + 1)
    dp[0] = 1  # nC0 is 1

    for i in range(1, n + 1):
        # Compute next row of Pascal's triangle using the previous row
        for j in range(min(i, k), 0, -1):
            dp[j] = dp[j] + dp[j - 1]

    return dp[k]


# Get user input
n = int(input("Enter value of n: "))
k = int(input("Enter value of k: "))

# Check constraints
if k < 0 or k > n:
    print("Invalid input: k should be in range 0 to n.")
else:
    print(f"{n}C{k} = {nCr(n, k)}")
