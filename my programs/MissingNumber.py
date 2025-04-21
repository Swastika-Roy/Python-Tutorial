def missing_num(arr):
    n = len(arr) + 1
    xor1 = 0
    xor2 = 0

    for num in arr:
        xor2 ^= num

    for i in range(1, n + 1):
        xor1 ^= i

    return xor1 ^ xor2
