#!/usr/bin/python3
""" Module: defines a locked class """


class LockedClass:
    """ Prevents the user from dynamically create new instance
        attributes, except if its called first_name
    """
    __slots__ = ['first_name']
