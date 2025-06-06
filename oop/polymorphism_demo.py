import math

class Shape:
    def area(self):
        """
        Base method to be overridden by derived classes.
        Raises NotImplementedError if not implemented in a subclass.
        """
        raise NotImplementedError("The area method must be implemented by the subclass.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initialize the Rectangle class with length and width.
        :param length: int or float, the length of the rectangle
        :param width: int or float, the width of the rectangle
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate the area of the rectangle.
        :return: int or float, the area of the rectangle
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """
        Initialize the Circle class with radius.
        :param radius: int or float, the radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        :return: float, the area of the circle
        """
        return math.pi * self.radius ** 2



