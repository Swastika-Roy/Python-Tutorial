# def Average(a,b):      #parametrised fun
#     print("Average = ", (a+b)/2)
#
#
# def Average(a=5, b=6):       #default fun
#     print("Average = ", (a + b) / 2)
#
# Average();
# Average(2,3)
#
#
# def Name(fname,mname = "kumar",lname = "Roy"):
#     print("Hello , ",fname,mname,lname)
# Name("Amar")

def Average(*numbers):
    print(type(numbers)) #list
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

d = Average(1,2)
print(d)

# def Name(** name):
#     print(type(name)) #dict
#     print("Hello! ",name["fname"],name["mname"],name["lname"])
#
# Name(fname="Swarup",mname="Kumar",lname="Roy")