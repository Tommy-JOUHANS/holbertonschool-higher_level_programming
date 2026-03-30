#!/usr/bin/python3
class LockedClass:
    __slots__ = ["first_name"]
    AttributeError = "LockedClass' object has no attribute 'last_name'"
