#!/usr/bin/python3
"""
This module implements a function that returns True is obj
is an instance of a class that inherited (directly or indirectly)
from a specified class
"""


def inherits_from(obj, a_class):
    """
    the implementation
    """

    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
