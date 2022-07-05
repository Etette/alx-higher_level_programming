#!/usr/bin/python3
"""
json
"""


class Student:
    """ A student class"""
    def __init__(self, first_name, last_name, age):
        """initialize student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dict rep of student instance"""
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            d = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    d[k] = v
            return d
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reload from json"""
        for (key, value) in json.items():
            setattr(self, key, value)
