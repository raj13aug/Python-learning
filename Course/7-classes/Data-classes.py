from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)

# Id function use to where an object is stored in memory.
print(id(p1))
print(id(p2))

print(p1 == p2)

#classes that have only data and no methods, you might want to use name tuple.
#class variable is immutable. which means we cannot modify.

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)

print(p1 == p2)
