#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for i in range(x):
        try:
            print(my_list[i], end=" ")
            a += 1
        except:
            continue
    print()
    return (a)
