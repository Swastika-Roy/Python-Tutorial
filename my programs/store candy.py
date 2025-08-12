def minMaxCandy(prices, k):
    # Sort the array to arrange candies by price
    prices.sort()

    n = len(prices)

    # Calculate minimum cost
    minCost = 0
    i, end = 0, n - 1
    while i <= end:
        minCost += prices[i]
        i += 1

        # seller gives k candies for free from the end
        end -= k

        # Calculate maximum cost
    maxCost = 0
    i, start = n - 1, 0
    while i >= start:
        maxCost += prices[i]
        i -= 1

        # seller gives k cheapest candies for free
        start += k

    return [minCost, maxCost]


if __name__ == '__main__':
    prices = [3, 2, 1, 4]
    k = 2
    res = minMaxCandy(prices, k)
    print(res[0], res[1])