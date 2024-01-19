import json
import os
import copy
# from models.base_model import BaseModel
import importlib
from datetime import datetime
""" The class FileStorage contains data serialization methods.

Attributes:
    __file_path (str): Defines the file path to the JSON FileStorage.
    __objects (dict): A dictionary that contains objects stored in FileStorage.

Methods:
    all(): Returns the __objects dictionary.
    new(obj): Sets in __objects the obj with key <obj class name>.id.
    save(): Serializes __objects to the JSON file (path: __file_path).
    reload(): Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists).

Note:
    This class is designed for handling data serialization and deserialization.
"""

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def __init__(self):
        pass

    def all(self):
        """Returns the __objects dictionary."""
        return FileStorage.__objects
        
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        
        # obj_copy = copy.deepcopy(obj)
        # self.temp_dict = obj.to_dict()
        # self.class_name = self.temp_dict.pop('__class__', None)
        # self.key = f"{self.class_name}.{str(obj.id)}"
        # # obj_copy.updated_at = obj_copy.updated_at.isoformat()
        # # obj_copy.created_at = obj_copy.created_at.isoformat()
        # FileStorage.__objects[self.key] = obj_copy
        # # print(obj_copy.__dict__)
        # print("in new method")
        # print(FileStorage.__objects)
        # print("in new method")
        
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        ser_dict = copy.deepcopy(FileStorage.__objects)
        for key, obj in ser_dict.items():
            new_obj = obj.to_dict()
            ser_dict[key] = new_obj
        
        # new_dict = copy.deepcopy(FileStorage.__objects)
        # print("in save method")
        # print(FileStorage.__objects)
        # print("in save method")
        # if type(new_dict) != dict:
        #     new_dict = new_dict.__dict__
        # # else:
        # #     # print("This is type of new_dict in save")
        # #     # print(type(new_dict))
        # for key,obj in new_dict.items():
        #     # print(type(obj))
        #     if type(obj) != dict:
        #         # print("i'm in")
        #         new_dict[key] = obj.__dict__
        #         # print(type(obj))
        #         # print(obj)
        #     new_dict[key]['updated_at'] = new_dict[key]['updated_at'].isoformat()
        #     new_dict[key]['created_at'] = new_dict[key]['created_at'].isoformat()
        # # print(new_dict)
        __objects_json = json.dumps(ser_dict)
        with open(FileStorage.__file_path, 'w') as file:
            file.write(__objects_json)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)."""
        if os.path.exists(FileStorage.__file_path) and os.path.getsize(FileStorage.__file_path) > 0:
            with open(FileStorage.__file_path, 'r') as file:
                data = file.read()
                deserialized_data = json.loads(data)
                for key, dict_obj in deserialized_data.items():
                    module_name = 'models.base_model'
                    module = importlib.import_module(module_name)
                    class_ = getattr(module, 'BaseModel')
                    instance = class_(**dict_obj)
                    FileStorage.__objects[key] = instance
                
            #     # FileStorage.__objects = deserialized_data
            #     for key, value in deserialized_data.items():
            #         # class_name, obj_id = key.split('.')
            #         module_name = 'models.base_model'
            #         module = importlib.import_module(module_name)
            #         class_ = getattr(module, 'BaseModel')
            #         instance = class_(**value)
            #         ####
            #         instance.updated_at = datetime.strptime(instance.updated_at.isoformat(),"%Y-%m-%dT%H:%M:%S.%f")
            #         instance.created_at = datetime.strptime(instance.created_at.isoformat(),"%Y-%m-%dT%H:%M:%S.%f")
            #         ####
            #         print("I'm key")
            #         print(key)
            #         print(instance)
            #         FileStorage.__objects[key] = instance
            #         # print(FileStorage.__objects[key])
            #         # print(instance)
            # print("in reload method")
            # print(FileStorage.__objects)
            # print("in reload method")
            
        
            # # FileStorage.__objects = BaseModel(my_dict)
        else:
            pass
