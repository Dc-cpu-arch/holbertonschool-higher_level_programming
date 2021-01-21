#!/usr/bin/python3
"""
Returns an Object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Returns data structure from JSON string"""
    return json.loads(my_str)
