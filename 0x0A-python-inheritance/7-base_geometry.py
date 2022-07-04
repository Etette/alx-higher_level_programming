#!/usr/bin/python3
"""
This module implements a base class for geometry object
"""


class BaseGeometry:
    """base class
    """
    def area(self):
        """ Raises exception for area()
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        checks the type of value and if value <= 0

        Args:
            name(str): name
            value(int): value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
