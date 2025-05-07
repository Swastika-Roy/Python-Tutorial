def luckyInteger(arr):
    arr.sort()
    ans = -1
    n = len(arr)
    i = 0

    while i < n:
        num = arr[i]
        count = 0

        while i < n and arr[i] == num:
             count += 1
             i += 1

        if num == count:
           ans = max(ans,num)

    return ans

lst = [1,2,2,3,3,3]
ans = luckyInteger(lst)
print(ans)

