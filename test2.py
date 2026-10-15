
class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)


p1 = Point(1, 2, 3)
p2 = Point(2, 3, 3)
p3 = Point(3, 4, 5)

print(p1+p2+p3)