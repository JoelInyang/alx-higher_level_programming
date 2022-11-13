#!/usr/bin/python3
"""
A class BG wuth public methods
of self and integer validator
"""


class BaseGeometry:
    """
    An empty class
    """
    pass


    def area(self):
        """
        it returns the area fo the BaseGeometry
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates integer input
        """
        if type(value) is not int:
            raise TypeError((name + "must be an integer"))
        if self.value < 0:
            raise ValueError(name + "must be greater than 0")
