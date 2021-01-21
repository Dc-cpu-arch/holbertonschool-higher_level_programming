#!/usr/bin/python3
"""
reads and prints contents from file
"""


def read_file(filename=""):
    """Reads and Prints"""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end='')
