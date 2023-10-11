#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = {x for x in my_list}
    return sum(new_set)
