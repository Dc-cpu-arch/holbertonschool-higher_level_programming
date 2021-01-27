#!/usr/bin/python3

import json


class Base():
    """ Base Object Absolute """

    __nb_objects = 0

    def __init__(self, id=None):
            if id is not None:
                self.id = id
            else:
                Base.__nb_objects += 1
                self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of Object Attributes"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the conversion from JSON str to type list"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string of attributes into an empty file"""
        name = cls.__name__ + ".json"
        objs = []
        if list_objs is not None:
            for ob in list_objs:
                objs.append(cls.to_dictionary(ob))
        with open(name, "w") as file:
            file.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """Returns a new instance made from Object Specified with
            dummy attributes"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of Base-Object (cls) instances made from
            JSON strings file"""
        name = cls.__name__ + ".json"
        instances = []
        try:
            with open(name, "r") as file:
                dictionaries = cls.from_json_string(file.read())
                for idx in dictionaries:
                    instances.append(cls.create(**idx))
        except FileNotFoundError:
            return []
        return instances
