#!/usr/bin/python3
""""
<a function that prints a square with the character #"
size is the size length of the square
size must be an integer, otherwise raise a TypeError
exception with the message size must be an integer
"""


def print_square(size):
    """function to print square"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
