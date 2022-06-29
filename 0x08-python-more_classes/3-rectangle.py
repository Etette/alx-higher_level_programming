#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """ Class that define a rectangle """

    def __init__(self, width=0, height=0):
        """Method that initializes the instance """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that returns the value of the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width nust be >= 0')
        self.__width = value

    @property
    def height(self):
        """method that returns the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """method that calculates area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """ method that calculates the perimeter of rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ method that returns the rectangle """
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle
        for i in range(self.height):
            rectangle += ("#" * self.width)
            if i == (self.height - 1):
                rectangle += "\n"

        return rectangle
