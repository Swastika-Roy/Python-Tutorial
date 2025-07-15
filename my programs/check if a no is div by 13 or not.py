def divBy13(s):
    # Stores running remainder
    rem = 0

    # Process each digit and compute remainder modulo 13
    for ch in s:
        rem = (rem * 10 + int(ch)) % 13

    # Final check for divisibility
    return rem == 0


if __name__ == "__main__":
    s = "2911285"

    if divBy13(s):
        print("true")
    else:
        print("false")