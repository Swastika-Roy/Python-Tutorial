def star(n):
  for i in range(1,n+1):
      for j in range(i,n+1):
          print("*",end=" ")
      print()

star(5)