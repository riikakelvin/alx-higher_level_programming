#!/usr/bin/python3
'''Defines a class and inherited class-checking function.'''

def is_kind_of_class(obj, a_class):
    """Checks whether an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check through
        a_class (type): The class to match the type of obj to.
    Returns:
        True - when obj is an instance or inherited instance of a_class.
        If not - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
