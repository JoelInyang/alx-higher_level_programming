#!/usr/bin/python3
def safe_print_integer(value):
    try:
        h = int()
        while (h):
            print("{:d}".format(value))
            return True
    except:
        return False

