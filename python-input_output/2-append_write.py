#!/usr/bin/python3
"""Module that defines a function  that appends a string at
the end of a text file (UTF8) and returns the number of characters added.

"""


def append_write(filename="", text=""):
    """ Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): filename to append to
        text (str): text to append to the file

    Raises:
        Exception: when the file can be opened.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
