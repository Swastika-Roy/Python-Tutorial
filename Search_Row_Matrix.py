class Solution:
    def search_row_matrix(self, mat, x):
        for row in mat:
            if self.binary_search(row, x):
                return True
        return False

    def binary_search(self, arr, x):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == x:
                return True
            elif x < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return False

# User input
def main():
    n = int(input("Enter number of rows: "))
    m = int(input("Enter number of columns: "))
    mat = []

    print("Enter the matrix rows (space-separated values):")
    for _ in range(n):
        row = list(map(int, input().split()))
        if len(row) != m:
            print("Each row must have exactly", m, "elements.")
            return
        mat.append(row)

    x = int(input("Enter the number to search for: "))

    sol = Solution()
    if sol.search_row_matrix(mat, x):
        print("Found")
    else:
        print("Not Found")

if __name__ == "__main__":
    main()
