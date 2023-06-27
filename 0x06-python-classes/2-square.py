#!/usr/bin/python3
'''Define a class Square'''
class Square:
    '''representation of a square'''
    def __init__(self, size=0):
        '''a new square assignment created'''
        if not isinstance(size, int):
            '''adition of size of new square created'''
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
