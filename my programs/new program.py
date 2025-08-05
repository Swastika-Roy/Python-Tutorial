class GfG:

    @staticmethod
    def is_palin_sent(s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            # Skip non-alphanumeric characters from left
            if not s[i].isalnum():
                i += 1
            # Skip non-alphanumeric characters from right
            elif not s[j].isalnum():
                j -= 1
            # If characters match (case-insensitive), move pointers
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            # If characters do not match, not a palindrome
            else:
                return False

        return True

# Main function
if __name__ == "__main__":
    s = "Too hot to hoot."
    print("true" if GfG.is_palin_sent(s) else "false")
