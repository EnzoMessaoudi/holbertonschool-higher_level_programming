#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    for i in range(idx + 1):
        if i == idx:
            return my_list[i]
