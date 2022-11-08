#!/usr/bin/python3
"""
Class of Rectangle with private attribute of width and height respectively
"""


class Rectangle:
    """
    Class of Rectangle with private attributes
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        It defines the width and return the width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        It returns the width value but first checks for errors
        and raises exceptions respectively
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """
        It defines the height and return the height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        It returns the height value but first checks for errors
        and raises exceptions respectively
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """
        It defines the area and returns the area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        It defines the perimeter and returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return None
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        It # prints along with print()
        """
        temp = ""
        if self.__width == 0 or self.__height == 0:
            return temp
        for i in range(self.__height):
            for j in range(self.__width):
                temp += '#'
                if i < self.__height - 1:
                    temp += '\n'
            return temp
