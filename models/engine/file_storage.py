#!/usr/bin/python3

"""this file is responsible for data persistence"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Responsible for data persistence
        __file: private class attribute (path to json)
        __objects: it stores all the object of class
    """

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    __file_path = 'file.json'
    __objects = {}

    def all(self) -> dict:
        """it returns all the object of a class"""
        return self.__objects

    def new(self, obj):
        """
        responsible for adding new object(instance) to the __object dictionary
        how it works:
            when a new object is created the new method is called
            to add the object(instance) to the dictionary storage,
            and we use the class name and objects id to create
            a unique key to identify each object in the dictionary
            storage.
            key construction:
                <obj class name>.<obj id>
                the value is the actual instance of the object
        use case:
            we use it to keep track of every object created during
            program's execution
            we also use it make sure each object is associated with
            a unique key base on it's class name and id making it easy
            to retrieve and manage instances
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        # print("this is the key", key)  # debugging

    def save(self) -> None:
        """it serializes the object before storage (json)"""
        serialized_obj = {}
        for k, v in self.__objects.items():
            serialized_obj[k] = v.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_obj, file, indent=2)

    def reload(self) -> None:
        """it serializes the json back to object"""
        if path.exists(self.__file_path) and path.getsize(self.__file_path) > 0:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                loaded_obj = json.load(file)
                for k, v in loaded_obj.items():
                    cl_name, obj_id = k.split('.')
                    # print("this is the class name", cl_name)  # for debugging
                    obj_cl = globals()[cl_name]
                    obj_instance = obj_cl(**v)
                    self.__objects[k] = obj_instance
                # print(f"Error decoding JSON in {self.__file_path}") # debugging
