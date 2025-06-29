# Python program to check if parentheses are balanced

def isBalanced(s):
    # Declare a stack to store the opening brackets
    st = []
    for i in range(len(s)):

        # Check if the character is an opening bracket
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            st.append(s[i])

        else:
            # If it's a closing bracket, check if the stack is non-empty
            # and if the top of the stack is a matching opening bracket
            if st and ((st[-1] == '(' and s[i] == ')') or
                       (st[-1] == '{' and s[i] == '}') or
                       (st[-1] == '[' and s[i] == ']')):

                # Pop the matching opening bracket
                st.pop()
            else:
                # Unmatched closing bracket
                return False

    # If stack is empty, return True (balanced), otherwise False
    return not st


if __name__ == "__main__":
    s = "{([])}"
    if isBalanced(s):
        print("true")
    else:
        print("false")