#!/usr/bin/python3
"""
writes in file and returns number of chars written
"""


def write_file(filename="", text=""):
    """Writes to text file and Returns characters written"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return(file.write(text))
