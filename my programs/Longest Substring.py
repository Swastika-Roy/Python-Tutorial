def longestKSubstr(s, k):
    n = len(s)

    # prefix frequency array: vec[i][ch] =
    # frequency of char 'a'+ch in s[0..i]
    vec = [[0] * 26 for _ in range(n)]

    for i in range(n):
        vec[i][ord(s[i]) - ord('a')] += 1
        if i > 0:
            for j in range(26):
                vec[i][j] += vec[i - 1][j]

    ans = -1

    # try for each starting index
    for i in range(n):

        # search space is from [i to n-1]
        low, high = i, n - 1
        currAns = -1

        while low <= high:
            mid = (low + high) // 2
            freq = vec[mid][:]

            # remove prefix before i if needed
            if i > 0:
                for j in range(26):
                    freq[j] -= vec[i - 1][j]

            # freq[j] -> represents the count of char('a' + j) in
            # the subtring starting from i and ending at mid
            count = sum(1 for f in freq if f > 0)

            if count == k:
                currAns = mid - i + 1
                low = mid + 1
            elif count < k:
                low = mid + 1
            else:
                high = mid - 1

        if currAns != -1:
            ans = max(ans, currAns)

    return ans


if __name__ == "__main__":
    s = "aabacbebebe"
    k = 3
    print(longestKSubstr(s, k))