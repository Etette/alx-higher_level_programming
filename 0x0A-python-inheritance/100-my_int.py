#!/usr/bin/python3
"""
100-my_int: class MyInt implements int
"""


class MyInt(int):
    """
    MyInt implements int. (inherits from)
    """
    def __init__(self, number):
        """initialize number
        """
        self.number = number

    def __ne__(self, value):
        """check is value == number
        """
        return (self.number == value)

    def __eq__(self, value):
        """check if value != number
        """
        return (self.number != value)

    def __str__(self):
        """return string
        """
        return (str(self.number))
