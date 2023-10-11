#!/usr/bin/python3
"""
Adds two numbers integers or floats and returns the result as an integer
:param a : the first number.
:param b : the second number.
Return the sum of a and b as an integer.

"""


def add_integer(a, b=98):
    """
    prototype to add two integer
    the function takes two number
    and return the sum as an integer
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")

    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
