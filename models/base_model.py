#!/usr/bin/python3
import uuid
import datetime

"""
This module contains the BaseModel class
Attributes:
id (UUID): string with UUID
created_at (datetime): date and time created
updated_at (datetime): date and time updated
"""


class BaseModel():
    """
    BaseModel class
    Attributes:
    id (UUID): string holdin UUID
    created_at (datetime): date created
    updated_at (datetime): date updated
    """
    def __init__(self):
        """
        Initializes the BaseModel class
        Attributes:
        name (str): name of the user
        my_number (int): id number
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """
        String rep of a class
        """
        return "[" + self.__class__.__name__ + "]" + "(" + self.id + ")" +\
            str(self.__dict__)

    def save(self):
        """
        Saves an objec to  a JSON file
        """
        updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """
        returns a dictionary with all keys and values of __dict__
        also adds key class to the dictionary with class name
        """
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        return dict
