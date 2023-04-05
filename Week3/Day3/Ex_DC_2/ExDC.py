from math import pi

class Circle:

    def __init__(self, radius: float) -> None:
        self.radius = radius
        self.diameter = radius * 2

    @classmethod
    def from_diameter(cls, diameter: float):
        new_circle = cls(diameter / 2)
        return new_circle
    
    @property
    def area(self):
        area = pi * self.radius ** 2
        return area
    
    # +
    def __add__(self, other_circle):
        radius_combined = self.radius + other_circle.radius
        new_circle = Circle(radius_combined)
        return new_circle
    
    # <
    def __lt__(self, other_circle):
        return self.radius < other_circle.radius
    
    # >
    def __gt__(self, other_circle):
        return self.radius > other_circle.radius
    
    # ==
    def __eq__(self, other_circle):
        return self.radius == other_circle.radius
    
    def __str__(self) -> str: # For individual usage
        return f'{self.radius}, {self.diameter})'
    
    def __repr__(self) -> str: # For casws with large data collections (list with Circles)
        return f'(Radius: {self.radius}, Diameter: {self.diameter})'

c1 = Circle(2.0)
c2 = Circle.from_diameter(6.0)

print("Radius circle1", c1.radius)
print("Diameter circle1", c1.diameter)

print("Radius circle2", c2.radius)
print("Diameter circle2", c2.diameter)

print("Circle1 area", c1.area)
print("Circle2 area", c2.area)

c3 = c1 + c2

print("Radius circle3", c3.radius)
print("Diameter circle3", c3.diameter)

print(c3 > c1)

circles = [c3, c2, c1]
circles.sort()
print(circles[0].radius)
print(circles[-1].radius)

print(circles)



# class Circle:

#     def __init__(self, radius: float) -> None:
#         self.radius = radius
#         self.diameter = radius * 2

#     def __init__(self, size: float, type_of_size: str) -> None:
#         if type_of_size == 'radius':
#             self.radius = size
#             self.diameter = size * 2
#         elif type_of_size == 'diametr':
#             self.radius = size / 2
#             self.diameter = size
#         else:
#             raise ValueError("Invalid type_of_size")
        
# c3 = Circle.from_diameter(6.0)

