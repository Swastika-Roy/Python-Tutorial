# x = [1,2,3]
# print(dir(x))
# print(x.__add__)

# x = (1,2,3)
# print(dir(x))
# print(x.__class__)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age
        self.version = 1

p = Person("Sunaina",16)
print(p.__dict__)

print(help(Person))