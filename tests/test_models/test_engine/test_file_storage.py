#!/usr/bin/python3
""" This module contains test cases for file_storage
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import unittest


class TestFileStorage(unittest.TestCase):
    """ File Storage test class
    """

    def test_instance(self):
        """ Test if an instance of FileStorage is created wuth all attributes
        """
        self.assertIsInstance(storage, FileStorage)

    def test_all(self):
        """ Tests if all() method returns a dictionary
        """
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        """ Tests if a new instance is recorded
        """
        base_model_obj = BaseModel()
        key = f'{base_model_obj.__class__.__name__}.{base_model_obj.id}'
        self.assertIn(key, storage.all().keys())

    def test_save(self):
        """ Tests serialization of instances to Json
        """

    def test_reload(self):
        """ Checks JSON deserialization
        """


if __name__ == "__main__":
    unittest.main()
