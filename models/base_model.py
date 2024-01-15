#!/sr/bin/python3
"""
this is the uuid module in python it is used for the creation of unique id.
this is date and time module in python it helps us work with time.
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Base model class, this is the super class
    where every other class would inherit from

    Attributes
        id: it's a public instance attribute uuid4 string
        created_at: it's a public instance attribute, datetime
        updated_at: it's a public instance attribute, datetime

    Methods
        save: we use it to keep track of any
            change made to the instance BaseModel
        to_dict: we use it to convert the data
        of each instance into a dictionary
        (first step of serialization/deserialization)
    """
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.
        Args:
            - *args: its not used
            - **kwargs: i's a dictionary of key-values arguments
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k in ['created_at', 'updated_at'] and\
                        isinstance(v, str):
                    v = datetime.strptime(v, self.TIME_FORMAT)
                setattr(self, k, v)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """returns the string representation of instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """helps save every created instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """helps convert object to dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        for k, v in obj_dict.items():
            if isinstance(v, datetime):
                obj_dict[k] = v.isoformat()
        return obj_dict
