def Transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix = [[1,2,3],[4,5,6]]
res = Transpose(matrix)
print("Original Matrix : ")
for row in matrix:
    print(row)
print("Transposed Matrix : ")
for row in res:
    print(row)