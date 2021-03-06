#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ Real Virtual Object """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        str_rep = ''
        if self.width == 0 or self.height == 0:
            return str_rep
        for i in range(self.height):
            str_rep += '#' * self.width
            if i < self.height - 1:
                str_rep += '\n'
        return str_rep

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
