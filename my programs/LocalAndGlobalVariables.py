x = 10 #global variable

def my_fun():
    global x
    x = 4

print(f" before using function, the value of x is {x}")

my_fun()

print(f" after using function, the value of x is {x}")