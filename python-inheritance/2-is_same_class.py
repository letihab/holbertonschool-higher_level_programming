#!/usr/bin/python3
"""
function that return True or False
if the object is exactly an instance
or not
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class."""

    if type(obj) == a_class:
        return True
    return False
