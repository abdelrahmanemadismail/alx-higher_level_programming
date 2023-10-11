#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    n = sum(score * weight for score, weight in my_list)
    d = sum(weight for _, weight in my_list)
    if d == 0:
        return 0
    return float(n) / d
