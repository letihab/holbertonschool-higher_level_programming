#!/usr/bin/python3
"""class definition of square"""


class Square:
    """class square defined"""

    def __init__(self, size=0):
        """initialize method"""
        self.__size = size

    @property
    def size(self):
        "property to retrieve it"
        return self.__size
    @size.setter
    def size(self, value):
        """property setter"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2