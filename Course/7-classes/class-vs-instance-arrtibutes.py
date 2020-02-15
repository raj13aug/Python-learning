''' Two attributers
    1, class  --> shared to comman also you can change the class variable
    2, Instance --> only for instance '''


# So class level attributers are shared across all instances of a class. If we change their value, the change is visble to all objects of that type

class Point:
    default_colour = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_colour = 'Yellow'
print(Point.default_colour)
Point.m = "Shamntha"                     # you can add the instance variable from hereitself 
Point.z = "Kurunaya"
point = Point('Raja', 'Mano')
print(point.x)
print(point.y)
print(point.z)
print(point.m)
