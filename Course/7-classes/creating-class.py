# I am using pascal naming convention, which is different from the naming convention that we use for naming our variable and function.

# Basically it says that the frist letter of every word should be upper case and there's no underscore here

# For example Class MyPoint

# All function in our classes should have at least one parameter.
# If use dot operator, you can see we have the draw method as well as a bunch of other methods that we didn't define. Through a mechanism called inheritance.
# isinstance, sometimes we have an object,if this object is an intance of a given class

# Point object need inital values like x and y, to set these values,we need a constructor


class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))