#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    boolean_list = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            boolean_list[count] = True
        else:
            boolean_list[count] = False
    return(boolean_list)

