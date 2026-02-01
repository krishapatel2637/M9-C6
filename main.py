class square:
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"The area of the square is {self.side**2}")


class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"The area of the rectangle is {self.length * self.breadth}")


class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"The area of the circle is {3.14 * self.radius * self.radius}")

obj1 = square(10)
obj2 = rectangle(10, 12)
obj3 = circle(10)

for shape in (obj1, obj2, obj3):
    shape.area()
