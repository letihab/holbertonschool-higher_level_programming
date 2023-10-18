#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle."""

    def __init__(self, width, height):
        """initializes width and height"""

        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
