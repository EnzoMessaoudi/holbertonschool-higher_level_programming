#!/usr/bin/python3

def pow(a, b):
    result = a

    for i in range(b - 1):
        if b < 0:
            result /= a
        result *= a
    return result
