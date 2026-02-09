#!/usr/bin/python3
"""Module that defines a function that writes to a file."""


def write_file(filename="", text=""):
    """ Function that writes a string to a text file (UTF8)
    and returns the number of characters written.

    Args:
        filename (str): filename to write to
        text (str): text to write to the file

    Raises:
        Exception: when the file can be opened.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
