class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):                          # convert object to string 
        return f"{self.x}, {self.y}"

    def draw(self):
        print(f"point ({self.x}, {self.y})")


point = Point('raj', 9)
print(point)

https://rszalski.github.io/magicmethods/
