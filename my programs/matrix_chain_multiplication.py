def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    # m[i][j] will hold the minimum number of multiplications needed to compute the matrix A[i]...A[j]
    m = [[0] * n for _ in range(n)]
    # s[i][j] will hold the index of the matrix after which the product is split
    s = [[0] * n for _ in range(n)]

    # l is the chain length
    for l in range(2, n + 1):  # l = 2 to n
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')  # Initialize to infinity
            for k in range(i, j):
                # q is the cost of multiplying A[i]...A[k] and A[k+1]...A[j]
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i + 1}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

# Example usage
if __name__ == "__main__":
    # Dimensions of matrices (A1: 10x20, A2: 20x30, A3: 30x40)
    p = [10, 20, 30, 40]  # p[i] is the number of rows of Ai and p[i+1] is the number of columns of Ai

    m, s = matrix_chain_order(p)

    print("Minimum number of multiplications is:", m[0][len(p) - 2])
    print("Optimal Parenthesization is: ", end="")
    print_optimal_parens(s, 0, len(p) - 2)
    print()