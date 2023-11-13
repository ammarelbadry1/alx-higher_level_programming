#!/usr/bin/python3
"""base Module.

This module represent a class Base.
"""
import json
import os


class Base:
    """Define a class Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance.

        Args:
            id (int): the id of the Base instance.
        """

        if (id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): the list to be serialized
        """

        if (not list_dictionaries):
            return '"[]"'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): the list to be serialized
        """

        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            if (list_objs is None):
                f.write("[]")
            else:
                list_objs = [o.to_dictionary() for o in list_objs]
                json_string = cls.to_json_string(list_objs)
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): the string to be deserialized
        """

        if (not json_string):
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            dictionary (dict): 
        """

        if (not dictionary):
            pass
        if cls.__name__ == "Rectangle":
            instance = cls(1, 2, 3, 4, 5)
        else:
            instance = cls(1, 2, 3, 4)
        instance.update(**dictionary)
        return instance
    
    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
