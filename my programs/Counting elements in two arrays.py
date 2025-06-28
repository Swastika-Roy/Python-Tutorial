def countLessEq(a, b):
    n = len(a)
    m = len(b)

    # Result array to store counts, initialized with zeros
    res = [0] * n

    # Pair each element of a[] with its original index to preserve order
    aIndexed = [(val, idx) for idx, val in enumerate(a)]

    # Sort the paired array and b[]
    aIndexed.sort()
    b.sort()

    ind = 0  # Pointer for b[]

    # For each element in sorted a[]
    for val, originalIndex in aIndexed:

        # Move ind until b[ind] > current val
        while ind < m and b[ind] <= val:
            ind += 1
        # Store the count at the correct position
        res[originalIndex] = ind

    return res


# Driver Code
if __name__ == "__main__":
    a = [1, 2, 3, 4, 7, 9]
    b = [0, 1, 2, 1, 1, 4]
    result = countLessEq(a, b)

    print(" ".join(map(str, result)))