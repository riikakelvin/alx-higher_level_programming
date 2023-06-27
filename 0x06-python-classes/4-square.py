#!/usr/bin/python3
'''defines a class square'''
class Square:
    '''representation of the square'''

    def __init__(self, size=0):
        '''assignment of a new square'''

        '''assigns a new square created'''
        '''arguement includes size and int'''
        self.size = size

    @property
    def size(self):
        '''defines size of present square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''displays size of current square area in play'''
        return (self.__size * self.__size)

