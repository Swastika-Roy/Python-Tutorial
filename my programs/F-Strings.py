from pytz import country_names

letter = "Hey My name is {1} and I am from {0}"

name = "Swastika"
country_names = "India"

# print(letter.format(country_names,name))
# print(f"Hey My name is {name} and I am from {country_names}")  #by using f"String"
print(f"Hey My name is {{name}} and I am from {{country_names}}")  #by using f"String"

# txt = "For only {price:.3f} dollars!"
# print(txt.format(price= 48.9989999))
#
# #by using f"String"
# price = 48.999999
# txt = f"For only {price:.2f} dollars!"
# print(txt)

print(type(f"{2*30}"))
