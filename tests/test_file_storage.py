#!/usr/bin/python3
"""Defines the unnittests cases for file_storage"""

import os
import unittest
from datetime import datetime
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models.engine.file_storage as bm_documentation

class Test_file_storage_documentation(unittest.TestCase):
    """Tests the documentation on the models/file_storage.py"""

    def test_bm_documentation(self):
        """tests the documantation on the file_storage file"""
        self.assertGreater(len(bm_documentation.__doc__), 0)

    def test_file_storage_save(self):
        """tests the documentation of the file_storage file"""
        self.assertGreater(len(BaseModel.save.__doc__), 0)

    def test_file_storage_toDict(self):
        """tests the documentation of the file_storage file"""
        self.assertGreater(len(BaseModel.to_dict.__doc__), 0)

    def test_file_storage_init(self):
        """tests the documentation of the file_storage file"""
        self.assertGreater(len(BaseModel.__init__.__doc__), 0)

    def test_file_storage_str(self):
        """tests the documentation of the file_storage file"""
        self.assertGreater(len(BaseModel.__str__.__doc__), 0)

class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the file_storage class."""
    
    def test_storage_initializes(self):
        self.assertEqual(type(FileStorage.filstorage), FileStorage)

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    

