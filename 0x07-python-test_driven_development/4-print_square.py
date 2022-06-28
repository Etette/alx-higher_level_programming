#!/usr/bin/python3
"""
This module defines 'print_square'

The function prints a sqaure
"""


def print_sqaure(size):
    """prints a square with size, 'size'"""
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for x in range(size):
        print('#' * size)
