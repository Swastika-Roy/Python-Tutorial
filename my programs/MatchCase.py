x = int(input("Enter number = "))

match x:
    case 0:
        print("x is zero")
    case  1:
        print("x is 1")
    case _ if x!=5:
        print(x," is not 5")
    case _ if x != 6:
        print(x," is not 6")
    case _:
        print(x)
