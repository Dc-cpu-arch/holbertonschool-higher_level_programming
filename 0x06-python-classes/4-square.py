#!/usr/bin/python3
"""Object Module Class Square"""


class Square:
    """Instantiation of a Square Class Objtect"""

    def __init__(self, size=0):
        """Initialization of Instance"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """Gets size of the object and returns it"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value as the square's size"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns square's area"""
        return self.__size ** 2
