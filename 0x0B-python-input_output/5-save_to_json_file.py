#!/usr/bin/python3
'''
Writes Python Object to file using JSON notation
'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes Python obj to file using JSON representation'''
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
