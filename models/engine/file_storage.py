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
    __file_path = "models/engine/file.json"
    __objects = {}
    
    def __init__(self):
        pass

    def all(self):
        """Returns the __objects dictionary."""
        return FileStorage.__objects
        
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        obj_copy = copy.deepcopy(obj)
        self.temp_dict = obj.to_dict()
        self.class_name = self.temp_dict.pop('__class__', None)
        self.key = f"{self.class_name}.{str(obj.id)}"
        FileStorage.__objects[self.key] = obj_copy.__dict__
        
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        new_dict = copy.deepcopy(FileStorage.__objects)
        for obj in new_dict.values():
            print(obj)
            obj['updated_at'] = obj['updated_at'].isoformat()
            obj['created_at'] = obj['created_at'].isoformat()
        __objects_json = json.dumps(new_dict)
        with open(FileStorage.__file_path, 'w') as file:
            file.write(__objects_json)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)."""
        if os.path.exists(FileStorage.__file_path) and os.path.getsize(FileStorage.__file_path) > 0:
            with open(FileStorage.__file_path, 'r') as file:
                data = file.read()
                deserialized_data = json.loads(data)
                FileStorage.__objects = deserialized_data
                for key, value in deserialized_data.items():
                    # class_name, obj_id = key.split('.')
                    module_name = 'models.base_model'
                    module = importlib.import_module(module_name)
                    class_ = getattr(module, 'BaseModel')
                    instance = class_(**value)
                    ####
                    instance.updated_at = datetime.strptime(instance.updated_at.isoformat(),"%Y-%m-%dT%H:%M:%S.%f")
                    instance.created_at = datetime.strptime(instance.created_at.isoformat(),"%Y-%m-%dT%H:%M:%S.%f")
                    ####
                    print("I'm Value")
                    print(value)
                    FileStorage.__objects[key] = instance
                    print("I'm instance")
                    print(instance)
            # # FileStorage.__objects = BaseModel(my_dict)
        else:
            pass
