#!/usr/bin/python3
"""Module for XML serialization and deserialization of data.
This module provides two functions:
- serialize_to_xml(dictionary, filename): Serializes data to XML format and saves it to a file.
- deserialize_from_xml(filename): Reads XML data from a file and deserializes it back to a dictionary.

"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML format and save it to a file."""
    root = ET.Element("root")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Read XML data from a file and deserialize it back to a dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
