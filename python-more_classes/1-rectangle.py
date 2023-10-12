#!/usr/bin/python3
"""
create an empty class Rectangle,
that defines a rectangle
you are not allowed to import any module
"""


class Rectangle:
    """initialized method of class Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height 

    @property
    def width(self):
        """private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
