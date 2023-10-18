#!/usr/bin/python3
"""
function that returns an object
represented by a JSON string
"""


import json


def save_to_json_string(my_obj, filename):
    """function that returns an object"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
