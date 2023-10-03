#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char = ord(c)
        if 'a' <= c <= 'z':
            char = char - 32
        print("{:c}".format(char), end='')
    print()
