# Python program to find the length of the lps

# Function to find the length of the lps
def longestPalinSubseq(s):
    n = len(s)

    # Create two arrays: one for the current state (dp)
    # and one for the previous state (dpPrev)
    curr = [0] * n
    prev = [0] * n

    # Loop through the string in reverse (starting from the end)
    for i in range(n - 1, -1, -1):

        # Initialize the current state of dp
        curr[i] = 1

        # Loop through the characters ahead of i
        for j in range(i + 1, n):

            # If the characters at i and j are the same
            if s[i] == s[j]:

                # Add 2 to the length of the palindrome between them
                curr[j] = prev[j - 1] + 2
            else:

                # Take the maximum between excluding either i or j
                curr[j] = max(prev[j], curr[j - 1])

        # Update previous to the current state of dp
        prev = curr[:]

    return curr[n - 1]

if __name__ == "__main__":
    s = "bbabcbcab"
    print(longestPalinSubseq(s))