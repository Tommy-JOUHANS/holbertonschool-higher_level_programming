#!/usr/bin/python3
""" Module that defines a class Student that defines
a student by first_name, last_name and age.

"""


class Student:
    """ Student class that defines a student by: first_name, last_name and age.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that retrieves a dictionary
        representation of a Student instance.

        Args:
            attrs: list of strings, contains the attributes to represent
            in the dictionary representation of the Student instance

        Returns:
            A dictionary representation of a Student instance.
        """

        if attrs is None:
            return self.__dict__

        dict_rep = {}
        for attr in attrs:
            if hasattr(self, attr):
                dict_rep[attr] = getattr(self, attr)

        return dict_rep
