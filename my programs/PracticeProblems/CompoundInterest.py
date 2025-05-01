p = int(input("Enter principal : "))
r = int(input("Enter rate of interest : "))
t = int(input("Enter time : "))
amount = p * (1 + (r/100) ** t)
ci = amount - p
print("Compund Interest : ",ci)