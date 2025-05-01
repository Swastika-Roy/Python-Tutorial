def leapYear(y):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        print("Leap Year")
    else:
        print("No")
y = int(input("Enter year : "))
print(leapYear(y))