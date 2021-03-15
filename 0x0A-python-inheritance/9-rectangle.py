#!/usr/bin/python3
"""
Module: defines a class Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeometry """

    def __init__(self, width, height):
        """ method - init a Rectangle object """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ method - returns area of an instance """
        return (self.__width * self.__height)

    def __str__(self):
        """ method - returns a specific string """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
