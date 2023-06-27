#!/usr/bin/python3
'''defines a class square'''
class Square:
    '''representation of the square'''
    def __init__(self, size):
        '''assigns a new square created'''
        self.size = size

    @property
    def size(self):
        '''defines the size of current square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''displays current area of square in play'''
        return (self.__size * self.__size)

    def my_print(self):
        '''prints out the square with hush(#) sign'''
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
