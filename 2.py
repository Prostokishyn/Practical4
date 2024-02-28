class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

v1 = Vector(2, 3)
v2 = Vector(4, 5)
add = v1 + v2
sub = v1 - v2
print(add.x, add.y)
print(sub.x, sub.y)