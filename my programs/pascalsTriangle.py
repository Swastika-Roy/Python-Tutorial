class Solution:
    def nthRowOfPascalTriangle(self, n):
        n -= 1  # Convert to 0-based index
        res = []

        prev = 1
        res.append(prev)

        for i in range(1, n + 1):
            curr = (prev * (n - i + 1)) // i
            res.append(curr)
            prev = curr

        return res

# Take user input
if __name__ == "__main__":
    n = int(input("Enter the row number (1-based index): "))
    sol = Solution()
    row = sol.nthRowOfPascalTriangle(n)
    print("The {}-th row of Pascal's Triangle is:".format(n))
    print(row)
