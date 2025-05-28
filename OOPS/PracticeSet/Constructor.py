# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
# s1 = Person("ram",12)
# s2 = Person("shyam",13)
#
# print(s1.name,s1.age)
# print(s2.name,s2.age)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def personalinfo(self):
#         print(self.name,self.age)
#
# s1 = Person("ram",12)
# s2 = Person("shyam",13)
#
# s1.personalinfo()
# s2.personalinfo()

class Person:
    dept = "IT"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def personalinfo(self):
        print(self.name,self.age,Person.dept)

s1 = Person("ram",12)
s2 = Person("shyam",13)

s1.personalinfo()
s2.personalinfo()

