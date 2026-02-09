#!/usr/bin/python3
"""Module a function that returns the JSON representation
 of an object (string).

"""


import json


def to_json_string(obj):
    """Function that returns the JSON representation of an object (string).

    Args:
        obj: object to convert to JSON string

    Returns:
        JSON string representation of obj
    """

    return json.dumps(obj)
