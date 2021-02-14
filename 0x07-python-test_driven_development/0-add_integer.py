#!/usr/bin/python3

""" Module: contains a function that adds two integers """


def add_integer(a, b=98):
    """ a = first number
        b = second number (default 98)

    TypeError if parameters are not int or float
    Returns the sum of the two numbers
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
