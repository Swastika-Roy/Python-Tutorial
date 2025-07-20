# Python program for coin change problem.
# using space optimised dp

def count(coins, sum):
    n = len(coins)

    # dp[i] will be storing the number of solutions for
    # value i. We need sum+1 rows as the dp is
    # constructed in bottom up manner using the base case
    # (sum = 0)
    dp = [0] * (sum + 1)

    # Base case (If given value is 0)
    dp[0] = 1

    # Pick all coins one by one and update the table[]
    # values after the index greater than or equal to the
    # value of the picked coin
    for i in range(n):
        for j in range(coins[i], sum + 1):
            dp[j] += dp[j - coins[i]]

    return dp[sum]


if __name__ == "__main__":
    coins = [1, 2, 3]
    sum = 5
    print(count(coins, sum))