#!/usr/bin/python3
"""
Module
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an
    instance of the specified class, or False
    """
    return type(obj) == a_class
