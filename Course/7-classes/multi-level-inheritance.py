class Animal():
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


# chicken cannot fly,example of ihheritance abuse is around the concept
# Multi level inheritance significally incrase the complexity of your software.
class Chicken(Bird):
    pass
