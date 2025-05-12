def add(A,B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

A = [[1,2,3],[1,2,3]]
B = [[1,2,3],[1,2,3]]
result = add(A,B)
print(result)
