# function to compute Z-array
# z[i] = length of the longest substring starting at i
# that matches the prefix of s
def zFunction(s):
    n = len(s)
    z = [0] * n

    # [l, r] is the current segment that matches a prefix
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            # inside the z-box: reuse previously computed values
            z[i] = min(r - i + 1, z[i - l])
        # try to extend the match beyond the current z-box
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        # update the z-box if the match extended beyond
        # current right boundary
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z


def getLongestPrefix(s):
    n = len(s)
    z = zFunction(s)

    # traverse z-array to find position where
    # suffix equals prefix
    for i in range(n - 1, 0, -1):
        if z[i] == n - i:
            # s[i:] is a suffix that is equal to the
            # prefix of length n - i
            return i
    return -1


if __name__ == "__main__":
    s = "abcab"
    print(getLongestPrefix(s))