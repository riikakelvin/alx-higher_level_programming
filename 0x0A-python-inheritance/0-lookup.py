#!/usr/bin/python3
'''Defines the  object attribute lookup function.'''

def lookup(obj):
    '''Returns a list of an object's available attributes and methods.'''
    return (dir(obj))
