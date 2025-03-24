class Student:
    # Constructor with default parameters (simulates overloading)
    def __init__(self, name, age=18, major="Undecided"):
        self.name = name
        self.age = age
        self.major = major

    # Method to display student info
    def show_info(self):
        print(f"{self.name}, {self.age} years old, studying {self.major}")


# Creating instances with different numbers of arguments
student1 = Student("Alice")
student2 = Student("Bob", 20)
student3 = Student("Charlie", 21, "Computer Science")

# Calling methods on instances
student1.show_info()
student2.show_info()
student3.show_info()