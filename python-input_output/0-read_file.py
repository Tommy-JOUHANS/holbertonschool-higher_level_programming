#!/usr/bin/python3
"""Module that defines a function that reads from a file."""


def read_file(filename=""):
    """ Function that reads a text file

    Args:
        filename (str): filename to read from

    Raises:
        Exception: when the file can be opened.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
