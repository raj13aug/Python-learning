# you might have repeated that in mutiple classes.so in this case

# 1.inheritance  --> mechanism that allow us to define the common behavior or common function in one class and inheritance to another class
# 2.composition


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal:  child, Sub


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")

# Alow inherit the attributes of a base class.


m = Mammal()
m.eat()
print(m.age)
