#If you don't need an existing object and that's when we use a class method.

#Use factory method with these values and this way you can move the complexity of creating this object into a factory methods

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"point ({self.x}, {self.y})")


#point = Point('raj', 9)
point = Point.zero()
point.draw()
