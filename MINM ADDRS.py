def check(arr, k, m, days):
    bouquets = 0
    cnt = 0

    # iterate through the bloom
    # days of the flowers
    for flower in arr:
        if flower <= days:
            cnt += 1
        else:

            # if the current bloom day count
            # is greater than days, update
            # the bouquets and reset count
            bouquets += cnt // k
            cnt = 0

    bouquets += cnt // k

    # check if current bouquets are greater
    # than or equal to the desired
    # number of bouquets (m)
    return bouquets >= m


def minDaysBloom(arr, k, m):
    lo = 0
    hi = max(arr)
    res = -1

    while lo <= hi:
        mid = (lo + hi) // 2

        if check(arr, k, m, mid):

            # if the current mid is valid update the result
            # and adjust the search range
            res = mid
            hi = mid - 1
        else:

            # if the current mid is not valid
            # adjust the search range
            lo = mid + 1
    return res


if __name__ == "__main__":
    arr = [5, 5, 5, 5, 10, 5, 5]
    k = 3
    m = 2
    print(minDaysBloom(arr, k, m))