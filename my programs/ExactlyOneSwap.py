# Function to count distinct strings after one swap
def countStrings(s):
    n = len(s)

    # Array to count character frequencies
    map = [0] * 26
    ans = 0

    # Count valid swaps, avoiding duplicates
    for i in range(n):
        ans += (i - map[ord(s[i]) - ord('a')])
        map[ord(s[i]) - ord('a')] += 1

    # Check for any duplicate character
    for i in range(26):
        if map[i] > 1:
            ans += 1
            break

    return ans


if __name__ == "__main__":
    s = "geek"
    # Output the count of distinct strings after one swap
    print(countStrings(s))