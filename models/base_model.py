import uuid
from datetime import datetime
import json

""" The class Basemodel defines the general structure of a class """ 
class Basemodel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        
    def updated_at(self):
        return self.updated_at
    
    def save(self):
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    def to_dict(self):
        self.__class__ = type(self)
        inst_dict = self.__dict__
        inst_dict['__class__'] = 'Basemodel'
        return inst_dict
        
    def __str__(self):
        return "[Basemodel] " + "(" + self.id +") " +str(self.__dict__)
