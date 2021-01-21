#!/usr/bin/python3
'''
Returns dictionary descriptions with simple DS of JSON serializations
'''


def class_to_json(obj):
   '''Uses Dictionary description an JSON'''
    return obj.__dict__
