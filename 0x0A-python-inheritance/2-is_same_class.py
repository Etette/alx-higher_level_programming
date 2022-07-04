#!/usr/bin/python3
"""
2-is_same_class: is_same_class()
"""


def is_same_class(obj, a_class):
    """
    returns True if obj is an exact instance of a_class

    Args:
        obj: object checked
        a_class: specified class

    Return:
        True if obj isinstance(a_class)
    """
    if type(obj) is a_class:
        return True
    else:
        return False
