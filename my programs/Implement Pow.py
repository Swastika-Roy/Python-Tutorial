# Python program to calculate pow(b, e)

# Naive iterative solution to calculate pow(b, e)
def power(b, e):
    # Initialize result to 1
    pow = 1

    # Multiply b for e times
    for i in range(abs(e)):
        pow = pow * b

    if e < 0:
        return 1 / pow

    return pow


if __name__ == "__main__":
    b = 3.0
    e = 5
    res = power(b, e)
    print(res)