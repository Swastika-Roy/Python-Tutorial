def maxVarArr(arr):
    n = len(arr)
    maxm = arr[0]
    currmax = arr[0]

    for i in range(1,n):
        if arr[i-1] < arr[i]:
            currmax += arr[i]
        else:
            maxm = max(maxm,currmax)
            currmax = arr[i]

    maxm = max(currmax,maxm)
    return maxm

arr = [1,2,3,4,5]
ans = maxVarArr(arr)
print("Maxm val : ",ans)

