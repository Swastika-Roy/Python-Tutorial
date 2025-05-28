n = 151
temp = n
s = 0
while n!=0:
    r = n%10
    s = s*10 + r
    n //= 10
if s == temp:
    print("palindrome")
else:
    print("not")