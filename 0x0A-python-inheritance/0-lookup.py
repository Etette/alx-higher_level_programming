#!/usr/bin/python3
"""
Returns the list of available attributes and methosd of an object:
"""


def lookup(obj):
    """returns list of attributes and methods of obj

    Args:
    obj (Any): object

    Returns:
    list of atributes and members
    """
    return dir(obj)
