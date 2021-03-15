#!/usr/bin/python3
"""
Module: defines a class geometry
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square inherits from Rectangle """

    def __init__(self, size):
        """ method - init a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ method - returns the area of a square """
        return super().area()
