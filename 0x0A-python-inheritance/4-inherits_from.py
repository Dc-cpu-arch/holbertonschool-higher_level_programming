#!/usr/bin/python3
"""
Module : checks the instance of an object
"""


def inherits_from(obj, a_class):
    """ checks if a object is an instance of a class
    inheriting directly or indirectly from the
    specifies class of a class
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
