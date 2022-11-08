#!/usr/bin/python3
"""
Printing of square with the character #
"""
def print_square(size):
    """
    Square printed using size as parameter
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise  TypeError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        print(end="")
    for j in range(size):
        print("#", end=" ")
