#!/usr/bin/python3
"""
create class Rectangle,
that defines a rectangle
you are not allowed to import any module
"""


class Rectangle:
    """A Rectangle class with attributes width and height,
    methods area, perimeter, print, str, repr, and del, and
    class attribute number_of_instances that keeps track of # of instances,
    class attribute print_symbol which is used as symbol for printing,
    and static method bigger_or_equal that returns biggest rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        Rectangle.number_of_instances += 1

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

    def area(self):
        """return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    rect += str(self.print_symbol)
                except Exception:
                    rect += type(self).print_symbol
            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_& must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
