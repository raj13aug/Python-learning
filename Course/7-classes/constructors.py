# __init__ method is called a constructor, when we create a new point object.
# self is reference to a current point object.
# The methods that we define in a class should have at least one parameter, which convention is called self


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
