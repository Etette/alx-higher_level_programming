#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Returns c if a is less than b
    else, it returns a*b-c"""

    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
