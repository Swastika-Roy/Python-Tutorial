from collections import defaultdict

# Function to check if a character is a vowel
def isVowel(ch):
    return ch in 'aeiou'

# Function to count the number of balanced subarrays
def countBalanced(arr):
    n = len(arr)
    res = 0
    prefix = 0

    # Map to store frequency of prefix sums
    freq = defaultdict(int)

    # Initial prefix sum is 0 (empty prefix is considered balanced)
    freq[0] = 1

    # Traverse the array of strings
    for i in range(n):
        score = 0

        # Calculate net score of current
        # string: +1 for vowel, -1 for consonant
        for ch in arr[i]:
            if isVowel(ch):
                score += 1
            else:
                score -= 1

        # Update the running prefix sum
        prefix += score

        # If this prefix sum has been seen before,
        # then the subarray between previous and
        # current prefix is balanced
        res += freq[prefix]

        # Increment the frequency of this prefix sum
        freq[prefix] += 1

    return res

if __name__ == "__main__":
    arr = ["aeio", "aa", "bc", "ot", "cdbd"]
    print(countBalanced(arr))