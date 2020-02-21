class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2


# Are Overrriding or replacing a method in the base class, if we still want to executre this constructor and initialize the age of an animal.
# use super() function to get acess to the base class.

m = Mammal()
print(m.age)
print(m.weight)
