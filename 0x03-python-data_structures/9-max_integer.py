#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list and len(my_list) > 0:
        new_list = my_list.copy()
        new_list.sort()
        return new_list[len(new_list) - 1]
    return None
