#!/usr/bin/python3

"""Defines a function that creates an Object from a “JSON file”."""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The path and name of the JSON file to load.

    Returns:
        object: The Python object created from the JSON data.
    """
    with open(filename, "r") as file:
        return json.load(file)
