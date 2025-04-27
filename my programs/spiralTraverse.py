def spiral_traverse(matrix):
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from Left to Right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from Top to Bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from Right to Left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # Traverse from Bottom to Top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

# Get user input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter the matrix row by row (space-separated values):")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Call the function
spiral_order = spiral_traverse(matrix)

print("Spiral Traversal of the matrix:")
print(spiral_order)
