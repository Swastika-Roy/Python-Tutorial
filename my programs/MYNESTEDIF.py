num = 18
if (num < 0):
    print("Negative")
elif(num > 0):
    if(num <= 10):
        print("number is less than 10")
    elif(num >= 10 and num <= 20):
        print("number is between 11 and 20")
    else:
        print("greater then 20")
else:
    print("it is 0")
