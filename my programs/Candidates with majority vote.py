def findMajority(arr):
    count1 = 0
    count2 = 0
    ele1 = 0
    el2 = 0

    # First pass find two potential candidates
    for num in arr:
        if count1 == 0 and num != el2:
            ele1 = num
            count1 = 1
        elif count2 == 0 and num != ele1:
            el2 = num
            count2 = 1
        elif num == ele1:
            count1 += 1
        elif num == el2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    # Second pass verify actual counts of the candidates
    count1 = count2 = 0
    for num in arr:
        if num == ele1:
            count1 += 1
        if num == el2:
            count2 += 1

    votes = len(arr)
    res = []

    # Add valid candidates to the result
    if count1 > votes // 3:
        res.append(ele1)
    if count2 > votes // 3 and el2 != ele1:
        res.append(el2)

    # Ensure result is in increasing order (at most 2 elements)
    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]

    return res


if __name__ == "__main__":
    arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
    result = findMajority(arr)
    print(*result)