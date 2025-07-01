def maxMinHeight(arr, k, w):

    n = len(arr)

    maxHeight = 0

    # Try increasing the minimum height
    # as long as possible
    while True:
        days = k
        water = [0] * n
        possible = True

        for i in range(n):

            # Add previous watering effect
            if i > 0:
                water[i] = water[i - 1]

            currHeight = arr[i] + water[i]

            # Remove watering effect beyond window w
            if i >= w:
                currHeight -= water[i - w]

            # If current height is less than required
            if currHeight < maxHeight + 1:
                add = maxHeight + 1 - currHeight
                water[i] += add
                days -= add

                # If days become negative, not possible
                if days < 0:
                    possible = False
                    break

        # Break if we can't raise height further
        if not possible:
            break

        # Otherwise increase maxHeight
        maxHeight += 1

    return maxHeight

# Driver code
if __name__ == "__main__":
    arr = [2, 3, 4, 5, 1]
    k = 2
    w = 2

    print(maxMinHeight(arr, k, w))