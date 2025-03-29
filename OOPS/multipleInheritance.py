class Employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"the name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f"the dance is {self.dance}")

class DancerEmployee(Dancer,Employee):
    def __init__(self,name,dance):
        self.name = name
        self.dance = dance

O = DancerEmployee("Radha","kathak",)
print(O.dance)
print(O.name)
O.show()
print(DancerEmployee.mro())
