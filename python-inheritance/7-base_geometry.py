#!/usr/bin/python3
"""define a base geometry of class Basegeometry"""


class BaseGeometry:
    """empty class BaseGeometry"""

    def area(self):
        """check if the area is implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
