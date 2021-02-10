#!/usr/bin/python3
""" Definition of a Square Object """


class Square:
    """ Square attributes an methods """

    def __init__(self, size=0):
        """ Initializes the object for every instance """

        self.size = size

    @property
    def size(self):
        """   Gets information about an instance   """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets value as instance size """

        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Returns the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ Prints the square in stdout with '#' """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()
