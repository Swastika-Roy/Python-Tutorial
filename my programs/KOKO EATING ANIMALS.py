def kokoEat(arr, k):
    mx = max(arr)

    for speed in range(1, mx + 1):

        time = 0
        for i in range(len(arr)):

            # Time required to eat this pile
            # of bananas at current speed
            time += arr[i] // speed

            # 1 extra hour to eat the remainder
            # number of bananas in this pile
            if arr[i] % speed != 0:
                time += 1

        # If total eating time at current speed
        # is smaller than given time
        if time <= k:
            return speed

    return mx


if __name__ == "__main__":
    arr = [3, 6, 7, 11]
    k = 8
    print(kokoEat(arr, k))