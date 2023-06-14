#!/usr/bin/python3
def number_keys(a_dictionary):
    num_keys = 0

    list_of_keys = list(a_dictionary.keys())

    for i in list_of_keys:
        num_keys += i

    return (num_keys)
