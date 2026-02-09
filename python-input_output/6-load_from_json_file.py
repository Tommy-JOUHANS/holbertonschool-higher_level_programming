#!/usr/bin/python3
"""Module that defines  a function that creates an Object from a "JSON file."""


import json


def load_from_json_file(filename):
    """Function that creates an Object from a "JSON file".

    Args:
        filename: name of file to read from

    Returns:
        Object created from JSON file
    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
