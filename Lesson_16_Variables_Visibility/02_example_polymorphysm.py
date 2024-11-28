# Parent Class: Geometry
class Geometry:
    def __init__(self, *args, **kwargs):
        print('This is Geometry INIT!')
        pass

    def area(self):
        """
        Calculate the area of the geometry object
        """
        pass

    def perimeter(self):
        """
        Calculate the perimeter of the geometry object
        """
        pass


# Child Class 1: Rectangle (inherits from Geometry)
class Rectangle(Geometry):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__(length, width)

    def area(self):
        """
        Calculate the area of the rectangle
        Formula: area = length * width
        """
        return self.length * self.width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle
        Formula: perimeter = 2 * (length + width)
        """
        return 2 * (self.length + self.width)


# Child Class 2: Circle (inherits from Geometry)
import math


class Circle(Geometry):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius)

    def area(self):
        """
        Calculate the area of the circle
        Formula: area = pi * (radius * radius)
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate the circumference of the circle
        Formula: circumference = 2 * pi * radius
        """
        return 2 * math.pi * self.radius


class Obj:
    def __init__(self, obj):
        self.obj = obj

    def area(self):
        return self.obj.area()


# Usage Example
rectangle = Rectangle(5, 3)
# print("Rectangle Area:", rectangle.area())
# print("Rectangle Perimeter:", rectangle.perimeter())

circle = Circle(4)
# print("Circle Area:", circle.area())
# print("Circle Perimeter:", circle.perimeter())

obj1 = Obj(circle)
print(obj1.area())
obj1.obj = rectangle
print(obj1.area())

