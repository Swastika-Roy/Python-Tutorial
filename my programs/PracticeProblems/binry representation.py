def generateBinary(n):
    result = []

    for num in range(1, n + 1):
        temp = num
        binary = ""

        # Convert decimal number to binary
        while temp > 0:
            rem = temp % 2

            if rem == 0:
                binary += '0'
            else:
                binary += '1'

            temp = temp // 2

        # reverse to get correct order
        binary = binary[::-1]

        result.append(binary)

    return result


if __name__ == '__main__':
    n = 6
    binaries = generateBinary(n)

    for bin in binaries:
        print(bin, end=' ')
    print()