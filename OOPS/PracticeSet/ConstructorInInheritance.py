# class A:
#     def __init__(self):
#         print("I am  init in A")
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("I am init in B")
#
# b = B()


class A:
    def __init__(self):
        print("I am  init in A")

class B:
    def __init__(self):
        print("I am  init in B")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("I am init in C")

c = C()
