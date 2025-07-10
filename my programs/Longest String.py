base1 = 31
mod1 = 10 ** 9 + 7
base2 = 37
mod2 = 10 ** 9 + 9


# function to compute pair hash
def computeHash(s):
    h1 = 0
    h2 = 0
    p1 = 1
    p2 = 1

    for ch in s:
        val = ord(ch) - ord('a') + 1
        h1 = (h1 + val * p1) % mod1
        h2 = (h2 + val * p2) % mod2

        p1 = (p1 * base1) % mod1
        p2 = (p2 * base2) % mod2

    return (h1, h2)


# check if all prefixes of word exist in hash set
def allPrefixExist(word, hashSet):
    h1 = 0
    h2 = 0
    p1 = 1
    p2 = 1

    for i in range(len(word)):
        val = ord(word[i]) - ord('a') + 1
        h1 = (h1 + val * p1) % mod1
        h2 = (h2 + val * p2) % mod2

        if (h1, h2) not in hashSet:
            return False

        p1 = (p1 * base1) % mod1
        p2 = (p2 * base2) % mod2

    return True


# function to get the longest word whose all prefixes exist
def longestString(arr):
    hashSet = set()

    for word in arr:
        hashSet.add(computeHash(word))

    result = ""

    # check for each word
    for word in arr:
        if allPrefixExist(word, hashSet):
            # update result if word is longer or
            # lexicographically smaller
            if len(word) > len(result) or (len(word) == len(result) and word < result):
                result = word

    return result


if __name__ == "__main__":
    arr = ["ab", "a", "abc", "abd"]
    print(longestString(arr))