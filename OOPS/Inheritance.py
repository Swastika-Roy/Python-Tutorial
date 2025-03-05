class Employee:

    def __init__(self,name,id):
        self.name = name
        self.id = id


    def showDetails(self):
        print(f"Name of Employee is {self.name} and id is {self.id}")

class Programmer(Employee):
    def language(self):
        print("My language is python")

e1 = Employee("Swastika",1);
e1.showDetails()
e2 = Programmer("Raju",2)
e2.showDetails()
e2.language()