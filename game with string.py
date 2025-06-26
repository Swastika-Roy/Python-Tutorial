def minValue(s, k):
    n = len(s)
    # Count of each letter (a-z)
    alphabetCount = [0] * 26

    maxi = 0
    # Count frequency of each character
    for c in s:
        alphabetCount[ord(c) - ord('a')] += 1
        maxi = max(maxi, alphabetCount[ord(c) - ord('a')])

    maxFreq = 0

    # freq[i] = number of characters with frequency i
    freq = [0] * (maxi + 1)

    # Fill frequency bucket and track the maximum frequency
    for count in alphabetCount:
        if count > 0:
            freq[count] += 1
            maxFreq = max(maxFreq, count)

    # Remove k characters by reducing higher frequencies
    while k > 0 and maxFreq > 0:
        count_at_max = freq[maxFreq]
        if count_at_max <= k:

            # Can remove all characters at this frequency
            k -= count_at_max
            freq[maxFreq - 1] += count_at_max
            freq[maxFreq] = 0
            maxFreq -= 1
        else:

            # Partially remove only k characters
            freq[maxFreq] -= k
            freq[maxFreq - 1] += k
            k = 0

    # Calculate the result: sum of (freq^2 * number of chars with that freq)
    result = 0
    for i in range(1, maxi + 1):
        result += i * i * freq[i]

    return result


# Driver code
if __name__ == "__main__":
    s = "abbccc"
    k = 2
    print(minValue(s, k))