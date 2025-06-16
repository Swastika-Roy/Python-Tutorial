# Function to find the total cost of making
# each tower height equal to h.
def findCost(heights, cost, h):
    res = 0
    n = len(heights)
    for i in range(n):
        res += cost[i] * abs(heights[i] - h)
    return res

# Return the minimum possible cost of operation
# to bring all the towers of different height
# in height[0..n-1] to same height.

def minCost(heights, cost):
    n = len(heights)

    # Find the binary search range
    mini = min(heights)
    maxi = max(heights)

    low = mini
    high = maxi
    ans = 0

    while low <= high:

        mid = low + (high - low) // 2

        val1 = findCost(heights, cost, mid - 1)
        val2 = findCost(heights, cost, mid)
        val3 = findCost(heights, cost, mid + 1)

        # If mid is the bottom most value.
        if val2 <= val1 and val2 <= val3:
            ans = val2
            break

        # If mid falls in the first segment
        elif val1 >= val2 and val2 >= val3:
            low = mid + 1

        # If mid falls in the second segment
        elif val2 >= val1 and val3 >= val2:
            high = mid - 1

    return ans


if __name__ == "__main__":
    heights = [1, 2, 3]
    cost = [10, 100, 1000]
    print(minCost(heights, cost))