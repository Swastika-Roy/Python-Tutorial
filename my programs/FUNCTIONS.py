def CalculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def IsGreater(a,b):
    if(a > b):
        print(a," is greater")
    else:
        print(b," is greater or equal")

def IsLesser(a,b):
    pass   #pass is used to complete the function later

a = 9
b = 8
CalculateGmean(9,8)
IsGreater(9,8)