
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species


    def make_sound(self):
        print("Sound maid by animal")

class Dog(Animal):
    def __init__(self,name,bread):
        Animal.__init__(self,name,species = "DOG")
        self.bread = bread

    def make_sound(self):
        print("Bark!")

d = Dog("dog","doggerman")
d.make_sound()

a = Animal("DOG","DOG")
a.make_sound()
