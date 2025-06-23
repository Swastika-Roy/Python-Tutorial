# Function to add two strings and return the result
def addString(s1, s2):
    i = len(s1) - 1
    j = len(s2) - 1

    # initial carry is zero
    carry = 0

    # we will calculate and store the
    # resultant sum in reverse order in res
    res = []
    while i >= 0 or j >= 0 or carry > 0:
        total = carry
        if i >= 0:
            total += int(s1[i])
        if j >= 0:
            total += int(s2[j])
        res.append(str(total % 10))
        carry = total // 10
        i -= 1
        j -= 1

    # remove leading zeroes which are currently
    # at the back due to reversed string res
    while res and res[-1] == '0':
        res.pop()

    # reverse our final string
    return ''.join(reversed(res)) if res else "0"


# Function to find minimum sum using count array approach
def minSum(arr):
    # Count array to store frequency of each digit
    count = [0] * 10

    # Count occurrences of each digit
    for num in arr:
        count[num] += 1

    # Two strings for storing the two minimum numbers
    s1 = []
    s2 = []

    # Flag to alternate between s1 and s2
    firstNum = True

    # Traverse count array from 0 to 9
    for digit in range(10):
        while count[digit] > 0:
            if firstNum:
                if not (len(s1) == 0 and digit == 0):
                    s1.append(str(digit))
                firstNum = False
            else:
                if not (len(s2) == 0 and digit == 0):
                    s2.append(str(digit))
                firstNum = True
            count[digit] -= 1

    # Handle case where s1 or s2 might be empty
    if not s1:
        s1.append("0")
    if not s2:
        s2.append("0")

    return addString(''.join(s1), ''.join(s2))


if __name__ == "__main__":
    arr = [6, 8, 4, 5, 2, 3, 0]
    print(minSum(arr))