def roman_to_int(s):
    def get_value(c):
        if c == 'I':
            return 1
        elif c == 'V':
            return 5
        elif c == 'X':
            return 10
        elif c == 'L':
            return 50
        elif c == 'C':
            return 100
        elif c == 'D':
            return 500
        elif c == 'M':
            return 1000
        return 0  # For safety, in case of invalid input

    total = 0
    prev_value = 0

    # Loop from right to left
    for ch in reversed(s):
        current_value = get_value(ch)
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    return total

# 🔁 Example usage
print(roman_to_int("III"))      # Output: 3
print(roman_to_int("LVIII"))    # Output: 58
print(roman_to_int("MCMXCIV"))  # Output: 1994
