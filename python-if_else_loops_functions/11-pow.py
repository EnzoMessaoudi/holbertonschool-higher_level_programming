#!/usr/bin/python3

def pow(a, b):
    result = a
    for i in range(b - 1):
        result *= a
    return result
