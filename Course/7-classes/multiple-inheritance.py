Similar to mutli level inheritance,it's a source of issues.
Mutiple inheritance is not always a bad thing. because don't use it properly.

class Flyer:
    def greet(self):
        print("flyer")

class Swimmer:
    def greet(self):
        print("swim")

class Manager(Flyer, Swimmer):
    pass

manager = Manager()
manager.greet()

#Similar to mutli level inheritance,it's a source of issues.
#Mutiple inheritance is not always a bad thing. because don't use it properly.
