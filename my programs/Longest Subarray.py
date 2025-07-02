def totalElements(arr):
    # keeps frequency of elements
    # in the current window
    mp = {}
    i = j = 0
    n = len(arr)
    size = 0

    while j < n:

        # Add the current element
        # to the map (or update its count)
        mp[arr[j]] = mp.get(arr[j], 0) + 1

        # If we have more than 2 distinct elements
        # shrink from the left
        while len(mp) > 2:
            mp[arr[i]] -= 1

            # Remove the number completely
            # if its count becomes 0
            if mp[arr[i]] == 0:
                del mp[arr[i]]
            i += 1

            # update the longest size found so far
        size = max(size, j - i + 1)
        j += 1

    return size


if __name__ == "__main__":
    arr = [0, 1, 2, 2, 2, 2]
    print(totalElements(arr))