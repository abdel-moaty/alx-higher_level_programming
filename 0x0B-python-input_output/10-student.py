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
        to_json(self, attrs=None): Retrieves a dictionary representation.
    """
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
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
            attrs = self.__dict__.keys()
        else:
            attrs = [attr for attr in attrs if hasattr(self, attr)]
        return {attr: getattr(self, attr) for attr in attrs}
