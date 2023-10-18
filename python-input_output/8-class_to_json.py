#!/usr/bin/python3
"""
function that returns the dictionary description with simple
data structure for json serialization of an object.
"""


def class_to_json(obj):
    """return the dictionnary representation"""
    return obj.__dict__
