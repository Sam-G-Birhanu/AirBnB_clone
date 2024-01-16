import uuid
from datetime import datetime
import json
from engine.file_storage import storage

"""The Basemodel class defines a basic model structure.

Attributes:
    id (str): A unique identifier generated using UUID version 4.
    created_at (str): The timestamp when the object is created.
    updated_at (str): The timestamp representing the last update.

Methods:
    updated_at(): Returns the current value of the 'updated_at' attribute.
    save(): Updates the 'updated_at' attribute to the current timestamp.
    to_dict(): Converts the object to a dictionary for serialization.
    __str__(): Returns a human-readable string representation of the object.

Note: This class is designed to serve as a base for other models with common attributes and methods.
"""

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new Basemodel instance."""
        if kwargs:
            for key in kwargs.keys():
                if key == "id":
                    setattr(self, 'id' , kwargs[key])
                if key == "name":
                    setattr(self, 'name' , kwargs[key])
                if key == "my_number":
                    setattr(self, 'my_number' , kwargs[key])
                if key == "created_at":
                    setattr(self, 'created_at' , datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"))
                if key == "updated_at":
                    setattr(self, 'updated_at' , datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.name = ""
            self.my_number = ""
            self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            storage.new()
        
    def updated_at(self):
        """Return the current value of the 'updated_at' attribute."""
        return self.updated_at
    
    def save(self):
        """Update the 'updated_at' attribute to the current timestamp."""
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        storage.save()

    def to_dict(self):
        """Convert the object to a dictionary for serialization."""
        inst_dict = {'__class__' : 'BaseModel'}
        inst_dict.update(self.__dict__.copy())
        return inst_dict

    def __str__(self):
        """Return a human-readable string representation of the object."""
        return f"[Basemodel] ({self.id}) {str(self.__dict__)}"
