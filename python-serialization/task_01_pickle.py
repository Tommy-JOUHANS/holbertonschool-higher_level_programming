#!/usr/bin/python3
"""Module for serializing and deserializing a custom object using pickle."""

import pickle


class CustomObject:
    """A custom object with attributes and methods for serialization."""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle."""
        with open(filename, 'rb') as file:
            return pickle.load(file)
