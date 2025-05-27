a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))

d = b*b - 4*a*c #discriminant

if d >0 :
    x1 = (-b + d ** 0.5)/(2*a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print("Real values are : ",x1," ",x2)

elif d == 0:
    x = -b / (2*a)
    print("one real value : ",x)

else:
    print("No real value")