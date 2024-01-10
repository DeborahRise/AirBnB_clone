#!/usr/bin/python3
'''
this is a uuid module in python it is used for the creation of unique id.
'''
import uuid
'''
this is date and time module in python it helps us work with time.
'''
from datetime import datetime

class BaseModel:
    def __init__(self,**kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_At = self.created_at
       


#__str__: should print: [<class name>] (<self.id>) <self.__dict__>
    def __str__(self):
        return  f"{[self.__class__.__name__]} {(self.id)} {self.__dict__} "
        # return f"{self.id} "

    def save(self):

        pass
    def to_dict(self):
        pass
   


base_Model_Istance = BaseModel()

print(base_Model_Istance)


# my_model = BaseModel()
# my_model.name = "My First Model"
# my_model.my_number = 89
# print(my_model)
# my_model.save()
# print(my_model)
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))