#!/usr/bin/python3
"""Locked class module"""


class LockedClass:
    """Prevents dynamic creation of instance attributes
    except for first_name"""
    __slots__ = ["first_name"]
