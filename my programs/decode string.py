# Function to decode given encoded string without using stack.

def decodedString(s):
    res = ""

    for i in range(len(s)):

        # If the current character is not a closing bracket, append it to the result string.
        if s[i] != ']':
            res += s[i]

        # If the current character is a closing bracket
        else:

            # Create a temporary string to store
            # the substring within the corresponding opening bracket.
            temp = ""
            while res and res[-1] != '[':
                temp = res[-1] + temp
                res = res[:-1]

            # Remove the opening bracket from the result string.
            res = res[:-1]

            # Extract the preceding number and convert it to an integer.
            num = ""
            while res and res[-1].isdigit():
                num = res[-1] + num
                res = res[:-1]
            p = int(num)

            # Append the substring to the result
            # string, repeat it to the required number of times.
            res += temp * p

    return res


if __name__ == "__main__":
    s = "3[b2[ca]]"
    print(decodedString(s))