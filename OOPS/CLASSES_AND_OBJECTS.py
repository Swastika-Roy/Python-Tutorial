class Person:
    name = "Titu"
    job = "Software_Enginner"
    netwoth = 10000

    def info(self):
       print(f"{self.name} is a {self.job} and her salary is {self.netwoth}")


a = Person()
a.name = "Swastika"

b = Person()
b.name = "Shraddha"
b.netwoth = 9000

a.info()
b.info()

# print(a.job)
# print(a.name)
# print(a.netwoth)