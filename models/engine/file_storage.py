import json
import os
from .models.base_model import BaseModel
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
        self.temp_dict = obj.to_dict()
        self.class_name = self.temp_dict.pop('__class__', None)
        self.key = f"{self.class_name}.{str(obj.id)}"
        FileStorage.__objects[self.key] = self.temp_dict
        # return FileStorage.__objects
        
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        __objects_json = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w') as file:
            file.write(__objects_json)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)."""
        if os.path.exists(FileStorage.__file_path) and os.path.getsize(FileStorage.__file_path) > 0:
            with open(FileStorage.__file_path, 'r') as file:
                data = file.read()
                my_dict = json.loads(data)
                
            FileStorage.__objects = BaseModel(my_dict)
        else:
            pass
