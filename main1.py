class Polygon:
    def __init__(self, side):
        self.side = side

s = input("Enter number of sides:")
p = Polygon(s)

print(p.side)

