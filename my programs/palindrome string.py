class Manacher:
    def __init__(self, s):

        # modified string with sentinels and separators
        self.ms = "@"
        for c in s:
            self.ms += "#" + c
        self.ms += "#$"

        # stores radius of palindromes centered
        # at each position in ms
        self.p = [0] * len(self.ms)

        # run the core algorithm
        self.runManacher()

    # core manacher's algorithm to compute radius array
    def runManacher(self):
        n = len(self.ms)
        l, r = 0, 0
        for i in range(1, n - 1):
            mirror = r + l - i

            # assign minimum radius based on mirror
            self.p[i] = max(0, min(r - i, self.p[mirror]))

            # expand palindrome centered at i
            while self.ms[i + 1 + self.p[i]] == self.ms[i - 1 - self.p[i]]:
                self.p[i] += 1

            # update the current rightmost boundary
            if i + self.p[i] > r:
                l = i - self.p[i]
                r = i + self.p[i]

    # return the length of longest palindrome centered at
    # cen in original string
    def getLongest(self, cen, odd):
        pos = 2 * cen + 2 + (0 if odd else 1)
        return self.p[pos]

    # check if substring s[l...r] is a palindrome
    # using precomputed radius
    def check(self, l, r):
        length = r - l + 1
        center = (r + l) // 2
        isOdd = length % 2
        return length <= self.getLongest(center, isOdd)


# function to count palindromic substrings of
# length >= 2
def countPS(s):
    m = Manacher(s)
    total = 0

    for val in m.p:
        # add ceil of (radius + 1) / 2 to count
        total += (val + 1) // 2

    # subtract the single-letter palindromes
    return total - len(s)


if __name__ == "__main__":
    s = "abbaeae"
    print(countPS(s))