#!/usr/bin/python3
"""
This module defines a Sqaure class

Its implements value and type checks for its attributes
"""


class Sqaure:
    """Square implementaation
    """
    def __init__(self, size=0):
        """initialize a square"""
        self.size = size

    @property
    def size(self):
        """get/set size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """set size """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """calculates the sqaure area
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints a square with the corresponding size
        """
        if (self.__size == 0):
            print('')

        for i in range(self.__size):
            print('#' * self.__size)
