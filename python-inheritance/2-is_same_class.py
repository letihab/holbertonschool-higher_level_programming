#!/usr/bin/python3
"""
function that return True or False
if the object is exactly an instance
or not
"""


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
