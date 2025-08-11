def manacherArray(s):
    # p[i] stores radius of palindrome centered
    # at i in the modified string
    ms = '@#' + '#'.join(s) + '#$'
    n = len(ms)
    p = [0] * n
    l = r = 0

    for i in range(1, n - 1):
        mirror = l + r - i
        if 0 <= mirror < n:
            p[i] = max(0, min(r - i, p[mirror]))

        while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 and
               ms[i + 1 + p[i]] == ms[i - 1 - p[i]]):
            p[i] += 1

        if i + p[i] > r:
            l = i - p[i]
            r = i + p[i]

    return p


# Returns length of longest odd/even
# palindrome centered at original index `cen`
def getLongest(cen, odd, p):
    pos = 2 * cen + 2 + (0 if odd else 1)
    return p[pos]


# Returns the maximum sum of lengths
# of two non-overlapping odd-length
# palindromic substrings
def maxSum(s):
    n = len(s)
    leftMark = [1] * n
    rightMark = [1] * n

    p = manacherArray(s)

    # Fill leftMark: maximum odd-length palindrome
    # ending at or before each index
    for i in range(n):
        val = getLongest(i, 1, p)
        li = i + val // 2
        if li < n:
            leftMark[li] = max(leftMark[li], val)

    for i in range(n - 2, -1, -1):
        leftMark[i] = max(leftMark[i], leftMark[i + 1] - 2)

    for i in range(1, n):
        leftMark[i] = max(leftMark[i], leftMark[i - 1])

    # Fill rightMark: maximum odd-length
    # palindrome starting at or after each index
    for i in range(n - 1, -1, -1):
        val = getLongest(i, 1, p)
        ri = i - val // 2
        if ri >= 0:
            rightMark[ri] = max(rightMark[ri], val)

    for i in range(1, n):
        rightMark[i] = max(rightMark[i], rightMark[i - 1] - 2)

    for i in range(n - 2, -1, -1):
        rightMark[i] = max(rightMark[i], rightMark[i + 1])

    # Combine the two arrays to compute the
    # maximum sum of disjoint palindromes
    ans = 0
    for i in range(n - 1):
        ans = max(ans, leftMark[i] + rightMark[i + 1])

    return ans


if __name__ == "__main__":
    s = "xyabacbcz"
    print(maxSum(s))