#!/usr/bin/python3
"""
3-is_kind_of_class : is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if obj is instance of a_class

    Args:
        obj: object checked
        a_class: specified class

    Return:
        True if isinstance(obj, a_class)
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
