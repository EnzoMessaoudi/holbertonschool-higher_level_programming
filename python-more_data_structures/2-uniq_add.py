#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    already_used = []

    for i in my_list:
        if any(i == x for x in already_used):
            continue
        result += i
        already_used.append(i)

    return result
