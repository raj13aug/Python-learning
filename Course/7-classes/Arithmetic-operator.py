class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 3)
other = Point(1, 3)
combined = point + other

print(combined.x)
