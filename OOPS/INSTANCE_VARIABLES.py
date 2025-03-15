class Employee:
    company = "APPLE"
    no_of_emp = 0
    def __init__(self,name):
        self.name = name
        self.raise_amt = 0.02
        Employee.no_of_emp += 1
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and raise amount in {self.no_of_emp} sized {self.company} is {self.raise_amt}")

e1 = Employee("Rohan")
e1.raise_amt = 0.3
e1.company = "Google"
# print(e1.raise_amt)
# print(e1.company)
# print(Employee.company)
Employee.showDetails(e1)
# e1.showDetails()
# Employee.showDetails(e1)
e2 = Employee("Ram")
e2.showDetails()
