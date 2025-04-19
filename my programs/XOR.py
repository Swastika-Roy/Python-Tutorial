def findMaximumXOR(arr):
    res = 0
    mask = 0

    for i in range(30, -1, -1):
        mask |= (1 << i)
        prefixes = set()

        for num in arr:
            prefixes.add(num & mask)

        candidate = res | (1 << i)

        for prefix in prefixes:
            if candidate ^ prefix in prefixes:
                res = candidate
                break

    return res

# --------- MAIN PROGRAM ---------
if __name__ == "__main__":
    # Take user input
    arr = list(map(int, input("Enter the numbers separated by space: ").split()))
    result = findMaximumXOR(arr)
    print("Maximum XOR of two numbers in the array is:", result)
