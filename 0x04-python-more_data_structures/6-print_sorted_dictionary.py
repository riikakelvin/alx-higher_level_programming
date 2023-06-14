#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list_dictionary = list(a_dictionary.keys())
    key_list_dictionary.sort()

    for i in key_list_dictionary:
        print ("{}:{}".format(i, a_dictionary.get(i)))

