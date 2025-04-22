from collections import defaultdict


def find_unique(arr):
    cnt = defaultdict(int)

    # Store frequency of each element
    for num in arr:
        cnt[num] += 1

    # Return the value with count = 1
    for num, count in cnt.items():
        if count == 1:
            return num

    # If no element exists that appears only once
    return -1