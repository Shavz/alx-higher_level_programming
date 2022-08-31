#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    i = sum([x * y for x, y in my_list])
    j = i / sum([y for x, y in my_list])
    return j
