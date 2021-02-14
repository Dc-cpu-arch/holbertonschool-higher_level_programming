#!/usr/bin/python3
""" Module to find the largest integer whitin a list """

def max_integer(list=[]):
    """ Find and return the largest value inside the list
    ---> The list must contain at least one element
    """
    if len(list) == 0:
        return None
    largest = list[0]
    i = 1
    while i < len(list):
        if list[i] > largest:
            largest = list[i]
        i += 1
    return largest
