#!/usr/bin/python3
"""
Import ABC (Abstract Base Class) and abstractmethod
from the abc module, these allow you to create abstract classes.

"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite représentant une forme géométrique."""

    @abstractmethod
    def area(self):
        """Retourne l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Retourne le périmètre de la forme."""
        pass


class Circle(Shape):
    """Représente un cercle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Représente un rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre d'une forme."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
