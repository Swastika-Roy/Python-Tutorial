# Python program to count number of
# ways to reach nth stair.

def minCostClimbingStairs(cost):
    n = len(cost)

    if n == 1:
        return cost[0]

    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    # Return minimum of cost to
    # climb (n-1)th stair and
    # cost to reach (n-2)th stair
    return min(dp[n - 1], dp[n - 2])


if __name__ == "__main__":
    cost = [16, 19, 10, 12, 18]
    print(minCostClimbingStairs(cost))