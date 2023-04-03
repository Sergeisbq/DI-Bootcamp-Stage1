# 1

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def square(self):
        return self.radius ** 2 * 3.14
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

circle_2 = Circle()
print(f"Circle's square is {circle_2.square()}")
print(f"Circle's perimeter is {circle_2.perimeter()}")


# 2

