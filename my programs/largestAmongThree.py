

# Example usage:
num1 = int(input("Enter the first number: "))
num2 =int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is greatest")
elif num2 >= num1 and num2 >= num3:
   print(f"{num2} is greatest")
else:
   print(f"{num3} is greatest")

