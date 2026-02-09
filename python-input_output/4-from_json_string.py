#!/usr/bin/python3
"""
Module that defines a function that returns an object (Python data structure)
represented by a JSON string.

"""

import json


def from_json_string(my_str):
    """Function that returns an object (Python data structure) represented
    by a JSON string.

    Args:
        my_str (str): JSON string to convert to Python data structure

    Returns:
        Python data structure represented by my_str
    """

    return json.loads(my_str)
