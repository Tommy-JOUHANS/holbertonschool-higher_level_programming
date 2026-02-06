#!/usr/bin/python3
"""
Import ABC (Abstract Base Class) and abstract method
from the abc module, these allow you to create abstract classes.

"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """ Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """ Return the area of the shape.
        """
        raise NotImplementedError("The area of the shape is not defined")

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape.
        """
        raise NotADirectoryError("The area of the shape is not defined")


class Circle(Shape):
    """ Class representing a circle.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """ Compute the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """ Compute the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """ Class representing a rectangle.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """ Compute the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """ Compute the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
