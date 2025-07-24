def getLastMoment(n, left, right):
    res = 0

    # Find the time to fall off the plank for all
    # ants moving towards left
    for i in range(len(left)):
        res = max(res, left[i])

    # Find the time to fall off the plank for all
    # ants moving towards right
    for i in range(len(right)):
        res = max(res, n - right[i])

    # Return the maximum time among all ants
    return res

if __name__ == "__main__":
    n = 4
    left = [2]
    right = [0, 1, 3]
    print(getLastMoment(n, left, right))