# a = input("Enter number : ")
# print(f"Table of {a} is : ")
#
# try:
#   for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except :
#     print("Invalid Input")
#
# print("Some important lines of code")
# print("End of Program")

try:
    num = int(input("Enter number : "))
    a = [6,3]
    print(a[num])
    
except ValueError:
    print("Number entered is not integer")

except IndexError:
    print("Index Error")
