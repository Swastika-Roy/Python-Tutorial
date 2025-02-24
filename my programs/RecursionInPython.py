#factorial
# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     return n*factorial(n-1)
#
# print(factorial(3))
#
# #at line 5 - 3*factorial(2)
# #at line 2 - factorial(2)
# #at line 5 - 2*factorial(1)
# #at line 3 - 2*1=2
# #at line 5 - 3*2

#Fibonacci Series
def fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(3))

# 0,1,1,2,3,5,8,13,21...