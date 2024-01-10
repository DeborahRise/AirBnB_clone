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
       updated_time = self.updated_At = datetime.today()
       return updated_time

#add the 'class' key with the class name as its valuep
    def to_dict(self):
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict



base_Model_Istance = BaseModel()
obj_to_dict = base_Model_Istance.to_dict()
save_obj = base_Model_Istance.save()
print("this is the saved version", save_obj)
print(obj_to_dict)

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