#!/usr/bin/python3
"""
Appends to text file and returns number of chars added
"""


def append_write(filename="", text=""):
    """Appends to text file and Returns number of chars added"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return(file.write(text))
