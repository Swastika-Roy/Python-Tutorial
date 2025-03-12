def reverse_integer(n):
    reversed_num = 0
    # Reverse the integer
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return  reversed_num

n = int(input("Enter number : "))
print("Reversed number : ",reverse_integer(n))

