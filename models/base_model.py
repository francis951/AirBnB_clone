#!/usr/bin/python3
"""Defition of a Base class"""

import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialize instances"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns string presentation
        returns:
                str:
                        class details
        """
        base_str = "["
        base_str += str(self.__class__.__name__) + "]("
        base_str += str(self.id) + ")" + str(self.__dict__)
        return base_str

    def save(self):
        """updates the public instance updated_at with the current datetime"""
        updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        Returns:
                dict:
                         keys/values
        """
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        return dict_obj
