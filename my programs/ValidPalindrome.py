class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and remove non-alphanumeric characters
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())

        # Check if the cleaned string is a palindrome
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True
