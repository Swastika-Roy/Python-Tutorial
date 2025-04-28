def rotate90_anticlockwise(mat):
    n = len(mat)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Step 2: Reverse each column
    for j in range(n):
        top = 0
        bottom = n - 1
        while top < bottom:
            mat[top][j], mat[bottom][j] = mat[bottom][j], mat[top][j]
            top += 1
            bottom -= 1


def print_matrix(mat):
    for row in mat:
        print(' '.join(map(str, row)))


# Main
n = int(input("Enter the size of the matrix (n x n): "))
mat = []

print("Enter the matrix row-wise:")
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

rotate90_anticlockwise(mat)

print("Rotated Matrix:")
print_matrix(mat)
