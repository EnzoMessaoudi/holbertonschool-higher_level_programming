#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    already_used = []

    for i in a_dictionary:
        smallest = None
        for j in a_dictionary:
            if j not in already_used:
                if smallest is None or j < smallest:
                    smallest = j
        print("{}: {}".format(smallest, a_dictionary[smallest]))
        already_used.append(smallest)
