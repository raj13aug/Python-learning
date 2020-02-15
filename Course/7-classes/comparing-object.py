class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(1, 3)
other = Point(1, 3)

print(point == other)

# Output will be false beacuse both object is different


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x == other.x and self.y == other.y


point = Point(10, 3)
other = Point(1, 3)

print(point == other)
print(point > other)
