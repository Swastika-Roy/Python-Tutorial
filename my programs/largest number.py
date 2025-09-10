def largestSwap(s):
    arr = list(s)
    maxDigit = '0'
    maxIndx, l, r = -1, -1, -1

    # Traverse from right to left
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > maxDigit:
            maxDigit = arr[i]
            maxIndx = i
        elif arr[i] < maxDigit:
            l, r = i, maxIndx

    if l == -1:
        return s

    # Perform swap
    arr[l], arr[r] = arr[r], arr[l]
    return "".join(arr)


if __name__ == "__main__":
    s = "768"
    print(largestSwap(s))