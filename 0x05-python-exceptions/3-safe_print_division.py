#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        temp = a/b
    except:
        temp = None
    finally:
        print("Inside result: {:d]".format(temp)
    return (temp)
