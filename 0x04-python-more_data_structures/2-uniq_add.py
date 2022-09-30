#!/usr/bin/python3
def uniq_add(my_list=[]):
    dup = set(my_list)
    add = 0
    for i in dup:
        add += 1
    return (add)
