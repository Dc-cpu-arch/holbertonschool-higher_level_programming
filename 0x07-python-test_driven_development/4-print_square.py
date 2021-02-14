#!/usr/bin/python3

""" Module: contains a function that prints a square with '#' """


def print_square(size):
    """ Size defines square's size, must be a possitive integer """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
