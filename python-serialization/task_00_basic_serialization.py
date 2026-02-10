#!/usr/bin/python3
"""Module for basic serialization
and deserialization of data to and from a file.
This module provides two functions:
- serialize_and_save_to_file(data, filename):
Serializes data to JSON and saves it to a file.

"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save it to a file."""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load data from a file and deserialize it from JSON."""
    with open(filename, 'r') as file:
        return json.load(file)
