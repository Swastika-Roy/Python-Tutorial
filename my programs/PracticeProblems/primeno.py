n=4
count = 1

for i in range(1,n):
    if n % i == 0:
        count+=1

if count == 2:
    print("prime")
else:
    print("not prime")