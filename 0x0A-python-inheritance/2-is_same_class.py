#!/usr/bin/python3
'''Defines a class-checking function.'''

def is_same_class(obj, a_class):
    """Checks whether an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check through
        a_class (type): The class to match the obj type to.
    Returns:
        If obj isan absolute instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
