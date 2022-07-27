class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    # In python, there are some default methods that are provided but are not defined.
    # Can find these methods by searching for python underscore methods.
    # If we want to perform + operation on point object, we need to define the __add__ method.
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    # This is called everytime we try to convert point object into string.
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # Finding the length of point from origin, to use this to compare points.
    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    # To get it to compare, we need to define those methods too.
    # Greater Than
    def __gt__(self, p):
        return self.length() > p.length()

    # Greater than or equal to
    def __ge__(self, p):
        return self.length() >= p.length()

    # Less than
    def __lt__(self, p):
        return self.length() < p.length()

    # Less than or equal to.
    def __le__(self, p):
        return self.length() <= p.length()

    # Equal to
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)

p5 = p1 + p2
p6 = p4 - p1
p7 = p2*p3

print(p5, p6, p7)

print(p1 == p2)
print(p1 > p2)
print(p4 < p3)