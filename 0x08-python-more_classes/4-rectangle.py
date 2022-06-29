#!/usr/bin/python3
"""
This module is composed by a class that defines a rectangle
"""


class Rectangle:
    """ class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ method that initializes the instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ methid that returns the value of the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('hieght must be >= 0')
        self.__height = value

    def area(self):
        """ method that calculates the Rectangle area"""
        return (self.width * self.height)

    def perimeter(self):
        """ method that calculates the Rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """method that returns the Rectangle #"""
        rectangle = ""
        if self.width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height):
            rectangle += ("#" * self.width)
            if i is not self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """ method that returns the string rep of the instance"""
        return "Rectangle({:d}, {:d}".format(self.__width, self.__height)
