#!/usr/bin/python3
"""
Write a function that creates
an Object from a “JSON file”:
"""


import json


def load_from_json_file(filename):
    """function that create an object from a json file"""
    with open(filename) as file:
        return json.loads(file)
