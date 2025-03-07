class Math:

    def __init__(self,num):
        self.num = num


    def addtonum(self,n):
        self.num = self.num + n


    @staticmethod    #here we does not require to add self it is called without self
    def add(a,b):
        return a + b

A = Math(5)
print(A.num)
A.addtonum(6)
print(A.num)
print(A.add(2,3))