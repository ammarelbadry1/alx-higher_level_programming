#!/usr/bin/python3
"""10-student Module

Define a class Student.
"""


class Student:
    """Represent a class Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): the list of attributes to be returned.
        """

        if attrs is None:
            return self.__dict__
        filtered_object_dict = {}
        for attr in attrs:
            try:
                filtered_object_dict[attr] = self.__dict__[attr]
            except KeyError:
                continue
        return filtered_object_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): the dictionary representation of another instance
        """

        try:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
        except KeyError:
            del self.first_name
            del self.last_name
            del self.age
