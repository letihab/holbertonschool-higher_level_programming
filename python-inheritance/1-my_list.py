#!/usr/bin/python3
"""
a class that inherits from list
"""


class MyList(list):
     """class that inherit from list"""
     
     def print_sorted(self):
        """function that prints the list, but sorted"""
        sorted_list = sorted(self)
        for item in sorted_list:
            print(item, end=' ')
