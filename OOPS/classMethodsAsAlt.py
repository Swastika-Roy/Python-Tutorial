class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls,string):
       name,salary = string.split(',')
       return cls(name,int(salary))

e1 = Employee("Harry",12000)
print(e1.name)
print(e1.salary)


e2 = Employee.fromStr("John,10000")
print(e2.name)
print(e2.salary)
