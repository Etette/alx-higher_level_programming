#!/usr/bin/python3
"""
A module composed by a class that defines a rectangle
"""


class Rectangle:
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """method that initializes the instance
        Args:
            width: width of triangle
            height: height of triangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """method that returns the value of the width
        Returns:
            width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """method that defines the width

        Args:
            value: width

        """
        if not isinstance(value, int):
            raise TypeError("width must be ann integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method that returns the value of the height
        Returns:
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """method that defines the height
        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value