class MathOperations:
    # Example of overloading using default arguments
    def add(self, a, b=0, c=0):
        return a + b + c

    # Example of overloading using variable-length arguments
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    # Example of overloading by checking types manually
    def concatenate(self, a, b):
        if isinstance(a, str) and isinstance(b, str):
            return a + b
        elif isinstance(a, int) and isinstance(b, int):
            return str(a) + str(b)
        else:
            raise ValueError("Unsupported types for concatenation")

# Create an instance of the class
math_ops = MathOperations()

# Using the add method with different numbers of arguments
print(math_ops.add(10))          # Output: 10
print(math_ops.add(10, 20))      # Output: 30
print(math_ops.add(10, 20, 30))  # Output: 60

# Using the multiply method with different numbers of arguments
print(math_ops.multiply(2, 3))        # Output: 6
print(math_ops.multiply(2, 3, 4))     # Output: 24
print(math_ops.multiply(2, 3, 4, 5))  # Output: 120

# Using the concatenate method with different types of arguments
print(math_ops.concatenate("Hello, ", "World!"))  # Output: Hello, World!
print(math_ops.concatenate(123, 456))             # Output: 123456