#!/usr/bin/python3
"""
Module: defines a class geometry
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
