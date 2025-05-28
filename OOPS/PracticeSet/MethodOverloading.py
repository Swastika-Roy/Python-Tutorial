# class Calculator:
#     def add(self,a=0,b=0,c=0):
#         return a+b+c
#
# calc = Calculator()
# print(calc.add(1,2,3))
# print(calc.add(1,2))
# print(calc.add(1))

class A:
    def sum(self,a=0,b=0,c=0):
        s=0
        if a != 0 and b != 0 and c != 0:
            s = a+b+c
        elif a!=0 and b!=0:
            s = a+b
        else:
            s=a
        return s

a = A()
print(a.sum(1,2,3))
print(a.sum(1,2))
print(a.sum(1))
print(a.sum())
