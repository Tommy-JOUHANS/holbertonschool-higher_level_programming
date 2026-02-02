#!/usr/bin/env python3
"""
Import ABC (Abstract Base Class) and abstractmethod
from the abc module, these allow you to create abstract classes.

"""


from abc import ABC, abstractmethod
"""
Definition of an abstract class.
Inheriting from ABC tells Python that this class
cannot be instantiated directly.

"""


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


"""
The Dog subclass inherits from Animal.

"""


class Dog(Animal):
    def sound(self):
        return "Bark"


"""
The cat subclass inherits from Animal.

"""


class Cat(Animal):
    def sound(self):
        return "Meow"
