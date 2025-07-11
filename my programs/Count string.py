# Function to multiply two 2x2 matrices
def multiply(mat1, mat2):

    # Perform matrix multiplication
    x = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    y = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    z = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    w = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]

    # Update matrix mat1 with the result
    mat1[0][0] = x
    mat1[0][1] = y
    mat1[1][0] = z
    mat1[1][1] = w

# Function to perform matrix exponentiation
def matrixPower(mat1, n):

    # Base case for recursion
    if n == 0 or n == 1:
        return

    # Initialize a helper matrix
    mat2 = [[1, 1], [1, 0]]

    # Recursively calculate mat1^(n/2)
    matrixPower(mat1, n // 2)

    # Square the matrix mat1
    multiply(mat1, mat1)

    # If n is odd, multiply by the helper matrix mat2
    if n % 2 != 0:
        multiply(mat1, mat2)

# Function to calculate the nth Fibonacci number
# using matrix exponentiation
def nthFibonacci(n):
    if n <= 1:
        return n

    mat1 = [[1, 1], [1, 0]]

    # Raise the matrix mat1 to the power of (n - 1)
    matrixPower(mat1, n - 1)

    return mat1[0][0]

# Function to count binary strings of length n
# that have at least one pair of consecutive 1's
def countConsec(n):
    # Total binary strings of length n = 2^n
    total = 1 << n
    # Count of strings without consecutive 1's = Fib(n + 2)
    noConsec = nthFibonacci(n + 2)
    return total - noConsec

if __name__ == "__main__":
    n = 3
    print(countConsec(n))