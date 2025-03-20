class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id


    def User_Info(self):
        print(f"User's name is {self.name} and id is {self.user_id}")

class Student(User):
    def __init__(self,name,user_id,roll,address):
      super().__init__(name,user_id)
      self.roll = roll
      self.address = address

    def User_Info(self):
        print("More info about student : ")
        print(f"{self.name}'s roll is {self.roll} her address is {self.address} and her id is {self.user_id}")


U = User("Swastika",1)
U.User_Info()

S = Student("Swastika",1,11,"Meghalaya")
S.User_Info()


