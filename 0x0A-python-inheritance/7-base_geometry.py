#!/usr/bin/python3
"""
A class BG wuth public methods
of self and integer validator
"""


class BaseGeometry:
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError((name + "must be an integer"))
        if self.value < 0:
            raise ValueError(name + "must be greater than 0")
