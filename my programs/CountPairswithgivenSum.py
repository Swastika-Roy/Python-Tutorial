from collections import defaultdict


def count_pairs(arr, target):
    freq = defaultdict(int)
    cnt = 0

    for num in arr:
        complement = target - num
        if complement in freq:
            cnt += freq[complement]
        freq[num] += 1

    return cnt


# User input section
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    target = int(input("Enter the target sum: "))

    result = count_pairs(arr, target)
    print("Number of pairs with sum", target, "is:", result)
