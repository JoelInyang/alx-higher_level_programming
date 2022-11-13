#!usr/bin/python3
"""
A class BG that raises exception
"""


class BaseGeometry:
    """
    It a BG class
    """
    def area(self):
        """
        A method for calculating thw function,
        it returns the function
        """
        raise Exception('area() is not implemented')
