#!/usr/bin/python3
"""A class BaseModel that defines all common attributes/methods for other classes."""

import models
from uuid import uuid4
from datetime import datetime

date_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
    """Base model for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """initialize a new Base model"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], date_format)
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], date_format)
            self.__dict__.update(kwargs)

    def __str__(self):
        """prints the updated_at instance of the super class"""
        s_class = self.__class__.__name__
        return "[{}]({}) {}".format(s_class, self.id, self.__dict__)
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
