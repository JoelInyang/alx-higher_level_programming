#!/usr/bin/python3
"""
A class Rectangle
"""
class Rectangle(BaseGeometry):
    """
    A class that inherit from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        s = self.integer_validator
        s("width", width)
        s("height", height)
