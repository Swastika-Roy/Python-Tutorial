def ascii_range_sums(s):
    positions = {}
    result = []

    # Step 1: Store first and last occurrence of each character
    for i, ch in enumerate(s):
        if ch not in positions:
            positions[ch] = [i, i]
        else:
            positions[ch][1] = i  # update last occurrence

    # Step 2: For each char with different first and last positions, calculate ASCII sum
    for ch, (start, end) in positions.items():
        if start != end:
            total = 0
            for i in range(start + 1, end):
                total += ord(s[i])
            if total != 0:
                result.append(total)

    return result

# --- User Input ---
s = input("Enter a string: ")
output = ascii_range_sums(s)
print("Output:", output)