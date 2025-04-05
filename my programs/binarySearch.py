arr = [1,2,3,4]
n = len(arr)
x = 4
l= arr[0]
r = arr[n-1]

while l<=m:
    m = (l + r) / 2
    if arr[m] == x:
        print("Found at ", m)
    elif arr[m]<x:
        l = m+1
    else:
       r=m-1
