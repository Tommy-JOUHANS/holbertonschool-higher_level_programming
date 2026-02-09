#!/usr/bin/python3
"""Module a function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file, after each line
    containing a specific string.

    Args:
        filename: name of file to read from and write to
        search_string: string to search for in file
        new_string: string to insert after each line containing search_string

    Raises:
        Exception: when the file can not be opened.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
