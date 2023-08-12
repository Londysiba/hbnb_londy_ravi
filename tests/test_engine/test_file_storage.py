#!/usr/bin/python3
"""Defines the unnittests cases for file_storage"""

import os
import unittest
import models
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
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileS_torage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    #def test_reload_no_file(self):
    #    self.assertRaises(FileNotFoundError, models.storage.reload())

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_method_returns_dictionary(self):
        """Test to returns the dictionary objects"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new_object_to_file_storage(self):
        """test to add new files to storage"""
        user = User()
        self.storage.new(user)
        obj_key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertTrue(obj_key in self.storage.all())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_save_to_file_storage(self):
        """test to serialize"""
        user = User()
        self.storage.new(user)
        self.storage.save()

        user = State()
        self.storage.new(user)
        self.storage.save()

        user = BaseModel()
        self.storage.new(user)
        self.storage.save()

        with open(FileStorage._FileStorage__file_path, 'r') as fileName:
            file_data = fileName.read()
            self.assertTrue(len(file_data) > 0)

    def test_reload_from_file_storage(self):
        """test to deserialize"""
        instances = [
            BaseModel(),
            User(),
            State(),
            Place(),
            City(),
            Amenity(),
            Review()
        ]

        for instance in instances:
            models.storage.new(instance)

        models.storage.save()
        models.storage.reload()

        #objs = models.storage._FileStorageobjects
        objs = models.storage._FileStorage__objects
        for instance in instances:
            self.assertIn(f"{instance.__class__.__name__}.{instance.id}", objs)

    def test_reload_no_file(self):
        """test to check if there's no file to deserialize"""
        try:
            models.storage.reload()
        except FileNotFoundError as e:
            self.assertEqual(str(e), "[Errno 2] No such file or directory: 'file.json'")

    

    

    
