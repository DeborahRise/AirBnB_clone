#!/usr/bin/python3
"""The FileStorage module"""

import os.path
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review
from models.city import City


class FileStorage:
    """Type class File Storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Type method all"""
        return FileStorage.__objects

    def new(self, obj):
        """Type method new"""
        FSobjdict = FileStorage.__objects
        object_name = obj.__class__.__name__
        FSobjdict["{}.{}".format(object_name, obj.id)] = obj

    def save(self):
        """Type method save"""
        FSobjdict = FileStorage.__objects
        obj_dict = {obj: FSobjdict[obj].to_dict() for obj in FSobjdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Type method reaload"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_d = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_d)(**obj))
            return
