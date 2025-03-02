class Person:

    # def __init__(self,n,j):
    #     print("HELLO INDIA!")
    #     self.name = n
    #     self.job = j

    def __init__(self):         #Default_Constructor
        print("HELLO INDIA!")

    def __init__(self, name, job):   #Parameterized_Constructor
        print("Intro :- ")
        self.name = name
        self.job = job

    def info(self):
        print(f"{self.name} is an {self.job}")


a = Person("Swastika","Engineer")
a.info()
b = Person("Shraddha","actor")
b.info()
# c = Person()

