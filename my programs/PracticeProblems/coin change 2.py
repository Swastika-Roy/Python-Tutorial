# Python program to find minimum of coins
def minCoins(coins, sum):
    # Initialize a list to store the minimum
    # number of coins for each amount
    dp = [float('inf')] * (sum + 1)

    # Base case: 0 coins are needed to make the sum of 0
    dp[0] = 0

    # Iterate over each coin in reverse order
    for i in range(len(coins) - 1, -1, -1):

        # Iterate through all amounts from 1 to sum
        for j in range(1, sum + 1):

            #  take variable for the current coin
            take = float('inf')

            #  noTake variable for the current amount
            noTake = float('inf')

            # If we can take the current coin
            if j - coins[i] >= 0 and coins[i] > 0:

                # Get the minimum coins needed
                # for the remaining amount
                take = dp[j - coins[i]]

                # Increment the count if it's a valid take
                if take != float('inf'):
                    take += 1

            # If there are coins left to consider
            if i + 1 < len(coins):
                # Get the minimum coins needed without
                # taking the current coin
                noTake = dp[j]

                # Store the minimum of taking or not
            # taking the current coin
            dp[j] = min(take, noTake)

    # Return the result for the given sum,
    # or -1 if it's not possible
    return dp[sum] if dp[sum] != float('inf') else -1


if __name__ == "__main__":
    coins = [9, 6, 5, 1]
    sum = 19
    print(minCoins(coins, sum))