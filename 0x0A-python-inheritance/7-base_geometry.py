#!/usr/bin/python3
"""
Module: definas a class geometry
"""


class BaseGeometry:
    """ defines geometry """

    def area(self):
        """ method - raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method - validates a value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".
                             format(name))
