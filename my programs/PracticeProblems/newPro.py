def assignHole(mices, holes):
    # Sort the arrays
    mices.sort()
    holes.sort()
    n = len(mices)
    # Finding max difference between
    # ith mice and hole
    Max = 0

    for i in range(n):
        if (Max < abs(mices[i] - holes[i])):
            Max = abs(mices[i] - holes[i])

    return Max


if __name__ == "__main__":
    mices = [4, -4, 2]
    holes = [4, 0, 5]

    # The required answer is returned
    # from the function
    minTime = assignHole(mices, holes)

    print(minTime)