def find_unique_number(nums):
    unique = 0
    for num in nums:
        unique ^= num
    return unique

# Taking user input
input_numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))

unique_number = find_unique_number(numbers)
print(f"The unique number is: {unique_number}")