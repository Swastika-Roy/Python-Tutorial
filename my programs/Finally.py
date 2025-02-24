# try:
#     l = [1, 2, 3, 4]
#     i = int(input("Enter index : "))
#     print(l[i])
# except:
#     print("Some error occured")
# finally:
#     print("I am always executed")


def func():
    try:
        l = [1, 2, 3, 4]
        i = int(input("Enter index : "))
        print(l[i])
        return 1

    except:
        print("Some error occured")
        return 0

    finally:
        print("I am always executed")
   # print("I am always executed")

x = func()
print(x)