# class A:
#     def feature1(self):
#         print("I am in feature 1")
#
# class B(A):
#     def feature2(self):
#         print("I am in feature 2")
#
# a = A()
# b = B()
# a.feature1()
# b.feature2()
# b.feature1()

# class A:
#     def feature1(self):
#         print("I am in feature 1")
#
# class B(A):
#     def feature2(self):
#         print("I am in feature 2")
#
# class C(B):
#     def feature3(self):
#         print("I am in feature 3")
#
# a = A()
# b = B()
# c = C()
# a.feature1()
# b.feature2()
# b.feature1()
# c.feature3()
# c.feature2()
# c.feature1()

# class A:
#     def feature1(self):
#         print("I am in feature 1")
#
# class B(A):
#     def feature2(self):
#         print("I am in feature 2")
#
# class C(B,A):
#     def feature3(self):
#         print("I am in feature 3")
#
#
# c = C()
# c.feature3()
# c.feature2()
# c.feature1()

# class A:
#     def feature1(self):
#         print("I am  feature 1 in A")
#
# class B:
#     def feature1(self):
#         print("I am  feature 1 in B")
#
# class C(A,B):
#     def feature2(self):
#         print("I am  feature 2 in C")
#
#
# c = C()
# c.feature1()

class A:
    def feature1(self):
        print("I am in feature1 in A")

class B:
    def feature1(self):
        print("I am in feature1 in B")

    def feature2(self):
        print("I am in feature2 in B")

class C(A,B):
    def feature3(self):
        super().feature1()
        super().feature2()
        print("I am in feature 3 in C")


c = C()
c.feature3()

