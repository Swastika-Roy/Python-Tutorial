class Employee:
    def __init__(self):
        self.name = "RAM"
        self.__id = 101   #private


    def _funname(self):     # "_" represents protected method
        return "Coding"

class Meeting(Employee):
    pass


obj = Employee()
obj1 = Meeting()

#calling by object of Employee class
print(obj.name)
print(obj._funname())


#Calling by object of Meeting
# Class
print(obj1.name)
print(obj1._funname())


# A = Employee()
# print(A.name)          #public
#
#
# print(A._Employee__id)      #private
#
# print(A.__dir__())