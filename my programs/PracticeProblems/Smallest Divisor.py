def smallestDivisor(arr, k):
    # Search space for binary search
    low = 1
    high = max(arr)
    res = -1

    while low <= high:
        mid = low + (high - low) // 2
        sum = 0

        # Calculate the total sum of quotient
        # using the current mid value
        for ele in arr:
            # Round off the quotient to the nearest greater integer
            sum += (ele + mid - 1) // mid

        if sum <= k:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res


if __name__ == "__main__":
    arr = [1, 2, 5, 9]
    k = 6
    print(smallestDivisor(arr, k))