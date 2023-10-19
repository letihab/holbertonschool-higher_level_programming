#!/usr/bin/python3
"""write a class Student that defines a student"""


class Student:
    """class student define"""

    def __init__(self, first_name, last_name, age):
        """initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionnary representation of student"""
        if attrs is not None:
            if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
                return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
