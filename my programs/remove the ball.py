# Python program to calculate the length after processing pairs

# Function to calculate the length after processing pairs
def findLength(color, radius):
    n = len(color)
    st = []

    for i in range(n):

        # If the top of the stack matches
        # current, pop it (remove both)
        if st and color[i] == color[st[-1]] and radius[i] == radius[st[-1]]:
            st.pop()
        else:
            st.append(i)

    # Return the number of elements
    # left in the stack
    return len(st)


if __name__ == "__main__":
    color = [2, 3, 5]
    radius = [3, 3, 5]

    print(findLength(color, radius))