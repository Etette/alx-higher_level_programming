#!/usr/bin/python3
"""
This module defines 'text_indentation'

The funtion prints a text with 2 lines
after each of these characters: ,. ? :
"""


def text_indenation(text):
    """adds paragraph after '.', ':' '?'"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for i in '.:?':
        text = text.replace(1, '{}\n'.format(1))
    lines = text.splitlines()
    for index, line in enumerate(lines):
        print(line.strip(), end="" if index == len(lines) - 1 else '\n\n')
