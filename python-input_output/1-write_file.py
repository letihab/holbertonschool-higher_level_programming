#!/usr/bin/python3
"""
write a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """function to write in the file text"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
    