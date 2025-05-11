def PeakEle(arr):
    n = len(arr)
    if len(arr) == 1 :
        return 0
    elif arr[0] > arr[1]:
        return 0
    elif arr[n-1]>arr[n-2]:
        return n-1
    else:
        st = 1
        end = n-2
        while st <= end:
            mid = st + (end-st)//2
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                st = mid+1
            else:
                end = mid-1
        return -1

arr = [1,2,3,1,2]
print("peak ele index : ",PeakEle(arr))