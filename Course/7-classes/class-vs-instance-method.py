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
