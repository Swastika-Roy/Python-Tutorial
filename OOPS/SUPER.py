# class Parent:
#     def parentMethod(self):
#         print("Parent Method ")
#
# class Child(Parent):
#     def parentMethod(self):
#         print("Harry2")
#         super().parentMethod()   # calling method using super keyword
#     def childmethod(self):
#         print("child method")
#         super().parentMethod()
#
# obj = Child()
# # obj.childmethod()
# obj.parentMethod()



class Manager:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class  Employee(Manager):
    def __init__(self,name,id,dept):      # calling constructor using super keyword
        super().__init__(name,id)
        self.dept = dept

M = Manager("SHUMAN",1)
E = Employee("RACHIT",1,"MANAGEMENT")
print(E.name)
print(E.id)
print(E.dept)