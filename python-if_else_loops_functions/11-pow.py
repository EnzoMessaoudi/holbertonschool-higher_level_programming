#!/usr/bin/python3

def pow(a, b):
    if b < 0:
        return a
    result = a
    for i in range(b - 1):
        result *= a
    return result
