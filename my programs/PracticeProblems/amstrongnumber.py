n = 153
temp = n
s= 0
while n!= 0:
    r = n%10
    s = s+(r*r*r)
    n //= 10

if temp == s:
    print("amstrong")
else:
    print("not")