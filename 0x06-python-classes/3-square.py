#!/usr/bin/python3
'''defines a class square'''
class Square:
    '''representation of the sqaure'''
    pass
    def __init__(self, size=0):
        '''assigns a new square created'''
        '''arguement includes size and int'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            return (self.__size * self.__size)
