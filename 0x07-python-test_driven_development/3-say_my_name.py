#!/usr/bin/python3
    """
    Firstname must be a string
    Lastname must also be a string
    """
    def say_my_name(first_name, last_name=""):
        """ Say your name and return nothing"""
        if type(first_name) is not string:
            raise TypeError('first_name must be a string')
        if type(last_name) is not string:
            raise TypeError('last_name must be a string')
        print("My name is {} {}".format(first_name, last_name))
