#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    s = 0
    try:
        num_list = [roman_numerals[c] for c in roman_string]
    except KeyError:
        return 0
    except TypeError:
        return 0
    len_list = len(num_list)
    mx = 0
    mx_index = 0
    for i in range(len_list):
        if num_list[i] >= mx:
            mx = num_list[i]
            mx_index = i
    for j in range(mx_index):
        s -= num_list[j]
    for z in range(mx_index, len_list):
        s += num_list[z]
    return s
