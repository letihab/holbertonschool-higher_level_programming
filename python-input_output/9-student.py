#!/usr/bin/python3
"""write a class Student that defines a student"""


class Student:
    """class student define"""

    def __init__(self, first_name, last_name, age):
        """initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionnary representation of student"""
        return self.__dict__
