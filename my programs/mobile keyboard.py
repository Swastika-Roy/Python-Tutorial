def getCount(n):
    ans = 0

    prev = [[1 for _ in range(3)] for _ in range(4)]
    prev[3][0] = 0
    prev[3][2] = 0

    curr = [[0 for _ in range(3)] for _ in range(4)]
    dir = [[0, 0], [0, -1], [0, 1], [-1, 0], [1, 0]]

    for k in range(2, n + 1):
        for i in range(4):
            for j in range(3):
                curr[i][j] = 0

                # For cell * and #
                if i == 3 and (j == 0 or j == 2):
                    continue

                # Check for all 5 next cells
                for d in dir:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < 4 and 0 <= y < 3:
                        curr[i][j] += prev[x][y]

        # Update previous states
        for i in range(4):
            for j in range(3):
                prev[i][j] = curr[i][j]

    # Add ans from each cell
    for i in range(4):
        for j in range(3):
            ans += prev[i][j]

    return ans


if __name__ == "__main__":
    n = 1
    print(getCount(n))