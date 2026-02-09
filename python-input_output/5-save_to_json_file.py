#!/usr/bin/python3
"""Module that defines a function that writes an Object to a text file.

"""


import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, using a JSON
    representation.

    Args:
        my_obj: object to write to file
        filename: name of file to write to

    Raises:
        Exception: when the file can not be opened.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f, ensure_ascii=False)
