#!/usr/bin/python3

"""
A base module for all other classes of the project
Parent Class
"""

import models
from datetime import datetime
from uuid import uuid4


class BaseModel:

    """ Base class 
    Defines a class Basemodel from which its subclasses will
    inherit from. This is the ADAM class
    """

    def __init__(self, *args, **kwargs):
        """ 
        Initializing the BaseModel
        """
        time_style = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs):
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_style))
                elif key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """ the save method of the base model """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """ 
        The magic class print format for the BaseModel 
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """ 
        Return a dict of all keys/values of __dict__

        """
        base_dict = self.__dict__.copy()
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        base_dict["__class__"] = self.__class__.__name__
        return base_dict
