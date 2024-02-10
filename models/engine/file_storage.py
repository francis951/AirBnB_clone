#!/usr/bin/python3

import os.path
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """A class to manage serialization and deserialization."""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialize_obj = {}
        for key, obj in FileStorage.__objects.items():
            serialize_obj[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialize_obj, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encodeing="utf-8") as file:
                read_file = file.read()
        except Exception:
            return
        the_obj = eval(read_file)
        for key, value in the_obj.items():
            the_obj[key] = eval(key.split(".")[0] + "(**value)")
        self.the_obj = the_obj

    def delete(self, obj):
        """Deletes obj from __objects"""
        try:
            key = obj.__class__.__name__ + "." + str(obj.id)
            del self.__objects[key]
            return True
        except Exception:
            return False
