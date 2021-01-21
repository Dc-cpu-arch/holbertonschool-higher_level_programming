#!/usr/bin/python3
'''
Returns the JSON representation of an str object
'''
import json


def to_json_string(my_obj):
    '''Gives the JSON representation of my_obj'''
    return json.dumps(my_obj)
