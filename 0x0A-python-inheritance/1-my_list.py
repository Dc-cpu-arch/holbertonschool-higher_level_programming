#!/usr/bin/python3
"""
Module
"""


class MyList(list):
    """ This class inherits from a list """
    def print_sorted(self):
        """ prints sorted lists """
        sorted_list = sorted(self)
        print(sorted_list)
