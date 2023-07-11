#!/usr/bin/python3

"""Defines a class Student that defines a student."""


class Student:
    """
    Represents a student.

    Public instance attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        __init__(self, first_name, last_name, age): Initializes a Student.
        to_json(self, attrs=None): Retrieves a dictionary representation.
        reload_from_json(self, json): Replaces all attributes of the Student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to be included.
            If None, all attributes will be included.

        Returns:
            dict: A dictionary containing the attributes of the Student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.

        Args:
            json (dict): The dictionary representing the attributes.
        """
        for attr, value in json.items():
            setattr(self, attr, value)
