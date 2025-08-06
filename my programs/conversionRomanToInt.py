def romanToDecimal(s):
    romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}

    res = 0
    i = 0
    while i < len(s):

        # if the current value is less than the next value,
        # subtract current from next and add to res
        if i + 1 < len(s) and romanMap[s[i]] < romanMap[s[i + 1]]:
            res += romanMap[s[i + 1]] - romanMap[s[i]]

            # skip the next symbol
            i += 1
        else:

            # otherwise, add the current value to res
            res += romanMap[s[i]]
        i += 1

    return res

if __name__ == "__main__":
    s = "IX"
    print(romanToDecimal(s))