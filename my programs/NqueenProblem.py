class Solution:
    def solveNQueens(self, n):
        def isSafe(row, col, board, n):
            # Check upper column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Check upper left diagonal
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check upper right diagonal
            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def solve(row, board, ans, n):
            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):
                if isSafe(row, col, board, n):
                    board[row][col] = 'Q'
                    solve(row + 1, board, ans, n)
                    board[row][col] = '.'  # backtrack

        ans = []
        board = [["."] * n for _ in range(n)]
        solve(0, board, ans, n)
        return ans
