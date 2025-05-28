class A:
    def feature1(self):
        print("I am in faeture 1 in A")

class B(A):
    def feature1(self):
        print("I am in feature 1 in B")

b=B()
b.feature1()
