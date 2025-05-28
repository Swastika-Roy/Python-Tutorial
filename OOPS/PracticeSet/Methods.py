class Person:
    dept = "IT"

    @classmethod
    def depinfo(cls):
        print(cls.dept)

    @staticmethod
    def otherinfo():
        print("It is not related to class nor dept")

p1 = Person()
p1.depinfo()
p1.otherinfo()