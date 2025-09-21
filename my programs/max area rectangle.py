def maxArea(mat):
    n, m = len(mat), len(mat[0])

    # memo[i][j] stores the width of consecutive 1's
    # ending at position (i, j).
    memo = [[0] * m for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                continue

            # Compute width of 1's at (i, j).
            memo[i][j] = 1 if j == 0 else memo[i][j - 1] + 1

            width = memo[i][j]

            # Traverse upwards row by row,
            # update minimum width and calculate area.
            for k in range(i, -1, -1):
                width = min(width, memo[k][j])
                area = width * (i - k + 1)
                ans = max(ans, area)

    return ans


if __name__ == "__main__":
    mat = [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0]
    ]

    print(maxArea(mat))