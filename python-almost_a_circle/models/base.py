#!/usr/bin/python3
"""create class base"""


class Base:
    """base model
    this is the base for all the task in that project"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id =  id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 
