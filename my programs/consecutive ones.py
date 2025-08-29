def maxOnes(arr, k):
    res = 0


    start = 0
    end = 0


    cnt = 0

    while end < len(arr):
        if arr[end] == 0:
            cnt += 1


        while cnt > k:
            if arr[start] == 0:
                cnt -= 1

            start += 1

        res = max(res, (end - start + 1))


        end += 1

    return res

if __name__ == "__main__":
    arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    k = 2
    print(maxOnes(arr, k))