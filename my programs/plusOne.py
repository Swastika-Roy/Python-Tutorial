def plus_one(digits):
    n = len(digits)

    # Handle case when last digit is not 9
    if digits[n - 1] != 9:
        digits[n - 1] += 1
        return digits

    digits[n - 1] = 0

    # Handle carry over
    for i in range(n - 2, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # All digits were 9
    return [1] + [0] * n

# --- Get user input ---
input_str = input("Enter digits separated by spaces (e.g. 1 2 3): ")
digits = list(map(int, input_str.strip().split()))

# Call function and print result
result = plus_one(digits)
print("Result after adding one:", result)
