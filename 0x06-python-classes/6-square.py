#!/usr/bin/python3

""" Definition of a Square Object """

class Square:
    """ Square Methods and Attributes """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialization of Square Instance """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Gets info about Instance size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size to the Instance """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value <= 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """ Gets info about Instance position

        Returns a tuple with square's position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position to the Instance """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if (type(value[0])) is not int or type(value[1]) is not int or
        value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ Returns Square's area """
        return self.__size ** 2

    def my_print(self):
        """ Displays the object in stdout with '#' """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
