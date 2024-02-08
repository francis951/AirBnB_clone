#!/usr/bin/python3

import os
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.objects[key] = obj

    def save(self):
        serialize_obj = {}
        for key, obj in FileStorage.__object.items():
            serialize_obj[key] = obj.to_dict
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(serialize_obj, f)

        def reload(self):
            """Deserializes the JSON file to __objects"""
            try:
                with open(self.__file_path, 'r') as file:
                    loaded_objs = json.load(file)
                    for key, obj_dict in loaded_objs.items():
                        class_name, obj_id = key.split('.')
                        obj_cls = eval(class_name)
                        obj = obj_cls(**obj_dict)
                        self.__objects[key] = obj
            except FileNotFoundError as e:
                print("Error loading JSON:", e)
                pass
