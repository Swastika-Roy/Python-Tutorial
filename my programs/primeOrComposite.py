def check_prime(num):
    if num <= 1:
        return "Neither prime nor composite"
    elif num == 2:
        return "Prime"
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return "Composite"
        return "Prime"

# Input from user
try:
    number = int(input("Enter a number: "))
    result = check_prime(number)
    print(f"The number {number} is {result}.")
except ValueError:
    print("Please enter a valid integer.")
