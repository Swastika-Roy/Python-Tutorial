def SumOfDigits(n):
    sum = 0
    while n > 0:
        r = n % 10
        sum += r
        n //= 10     #floor division
    return  sum
print(SumOfDigits(123))