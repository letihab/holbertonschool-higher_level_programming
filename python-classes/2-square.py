#!/usr/bin/python3
"""class definition of square"""


class Square:
    """class square defined"""

    def __init__(self, size = 0):
        """initialize method"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
        
