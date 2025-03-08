class Employee:

    company = "Apple"

    def show(self):
        print(f"{self.name} works in {self.company}")

    @classmethod
    def changecompany(cls, newcompany):
        cls.company = newcompany


a = Employee()
a.name = "Sohail"
a.show()
a.changecompany("Tesla")
a.show()
print(Employee.company)