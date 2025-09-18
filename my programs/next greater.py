def nextGreater(arr):
    n = len(arr)
    res = [-1] * n
    st = []

    for i in range(2 * n - 1, -1, -1):

        # Pop elements from the stack that are less
        # than or equal to the current element
        while st and st[-1] <= arr[i % n]:
            st.pop()

        # If the stack is not empty, the top element
        # is the next greater element
        if i < n and st:
            res[i] = st[-1]

        st.append(arr[i % n])

    return res


if __name__ == "__main__":
    arr = [5, 7, 1, 2, 6]
    ans = nextGreater(arr)
    for x in ans:
        print(x, end=" ")