arr = [1,2,3,4]
x = 4
n = len(arr)
if x in arr:
        index = arr.index(x)
        print("Found at ",index)
else:
  print("Not Found")