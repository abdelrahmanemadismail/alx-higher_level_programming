#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        printed_count = 0
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            printed_count += 1
        print()
        return printed_count
    except IndexError:
        print()
        return printed_count
