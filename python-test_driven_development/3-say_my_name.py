#!/usr/bin/python3
"""
 a function that prints My name is <first name> <last name>
 first_name and last_name must be strings otherwise,
 raise a TypeError exception with the message
first_name must be a string
last_name must be a string
"""


def say_my_name(first_name, last_name=""):
    """function to print my name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if last_name and not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
