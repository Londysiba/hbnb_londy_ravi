#!/usr/bin/python3
"""Defines the unnittests cases for base_model"""

import os
import unittest
import models
from time import sleep

from datetime import datetime
from models.base_model import BaseModel
import models.base_model as bm_documentation


class Test_base_model_documentation(unittest.TestCase):
    """Tests the documentation on the models/base_model.py"""

    def test_bm_documentation(self):
        """tests the documantation on the base_model file"""
        self.assertGreater(len(bm_documentation.__doc__), 0)

    def test_base_model_save(self):
        """tests the documentation of the base_model file"""
        self.assertGreater(len(BaseModel.save.__doc__), 0)

    def test_base_model_toDict(self):
        """tests the documentation of the base_model file"""
        self.assertGreater(len(BaseModel.to_dict.__doc__), 0)

    def test_base_model_init(self):
        """tests the documentation of the base_model file"""
        self.assertGreater(len(BaseModel.__init__.__doc__), 0)

    def test_base_model_str(self):
        """tests the documentation of the base_model file"""
        self.assertGreater(len(BaseModel.__str__.__doc__), 0)

class Test_base_model_initialization(unittest.TestCase):
    """tests the initialization method on base_model file"""

    def test_base_model_instances(self):
        """tests the instances of the base_model file"""
        b_model = BaseModel()
        self.assertTrue(type(b_model == BaseModel))
    
    def test_base_model_creationTime(self):
        """tests the created_at time of the base_model file"""
        b_model1 = BaseModel()
        sleep(0.02)
        b_model2 = BaseModel()
        self.assertGreater(b_model2.created_at, b_model1.created_at)

    def test_base_model_updatedTime(self):
        """tests the updated_at time of the base_model file"""
        b_model1 = BaseModel()
        sleep(0.03)
        b_model2 = BaseModel()
        self.assertGreater(b_model2.updated_at, b_model1.updated_at)

    def test_base_model_2_diff_id(self):
        """tests if 2 different id"""
        b_model1 = BaseModel()
        b_model2 = BaseModel()
        self.assertNotEqual(b_model1, b_model2)

    def test_base_model_uuid4(self):
        """tests if id is the type uf uuid4"""
        b_model1 = BaseModel()
        sleep(0.03)
        b_model2 = BaseModel()
        self.assertEqual(b_model1.id[14], '4')
        self.assertEqual(b_model2.id[14], '4')

    def test_unused_args(self):
        b_model = BaseModel(None)
        self.assertNotIn(None, b_model.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt_format = datetime.today()
        dt_iso_format = dt_format.isoformat()
        b_model = BaseModel(id="345", created_at=dt_iso_format,
                       updated_at=dt_iso_format)
        
        self.assertTrue(b_model.id == "345")
        self.assertTrue(b_model.created_at == dt_format)
        self.assertTrue(b_model.updated_at == dt_format)

    def test_of_None_kwargs_instantiation(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

class Test_base_model_str(unittest.TestCase):
    """tests the __str__ method on base_model file"""

    def test_base_model_id_string(self):
        """tests if the id is a string"""
        b_model = BaseModel()
        self.assertTrue(type(b_model.id) == str)

    def test_if_objStr(self):
        """tests if object is string"""
        b_model = BaseModel()
        b_model_result = f"{BaseModel}({id}){dict}"
        self.assertNotEqual(str(BaseModel), b_model_result)

class Test_base_model_save(unittest.TestCase):
    """Test cases for save method on base_model file"""

    @classmethod
    def setUpClass(cls):
        cls.backup_file_name = "tmp.json"
        cls.test_file_name = "file.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file_name):
            os.remove(cls.test_file_name)

    def test_base_model_save_dateTime(self):
        """tests for save method on base_model file"""
        b_model = BaseModel()
        sleep(0.03)
        updated_at1 = b_model.updated_at
        b_model.save()
        self.assertLess(updated_at1, b_model.updated_at)

    def test_bm_two_saves(self):
        """tests cases that save to base models"""
        b_model = BaseModel()
        first_updated_at = b_model.updated_at
        sleep(0.05)
        b_model.save()
        second_updated_at = b_model.updated_at
        self.assertTrue(first_updated_at < second_updated_at)
        sleep(0.05)
        b_model.save()
        self.assertTrue(second_updated_at < b_model.updated_at)

    def test_saveArgs(self):
        b_model = BaseModel()
        with self.assertRaises(TypeError):
            b_model.save(None)

    def test_save_updates_file(self):
        b_model = BaseModel()
        b_model.save()
        b_model_id = "BaseModel." + b_model.id
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertTrue(b_model_id in file_content)

class Test_base_model_to_dict(unittest.TestCase):
    """tests cases for to_dict on base_model file"""

    def test_base_model_to_dict(self):
        """test the to_dict method on the Basemodel"""
        b_model = BaseModel()
        self.assertTrue(isinstance(b_model.to_dict(), dict))

    def test_model_to_dict_keys(self):
        """tests the correct keys for the to_dict method on Base_model file"""
        b_model = BaseModel()
        keys = ["id", "created_at", "updated_at", "__class__"]
        self.assertIn("id", b_model.to_dict())
        self.assertIn("created_at", b_model.to_dict())
        self.assertIn("updated_at", b_model.to_dict())
        self.assertIn("__class__", b_model.to_dict())

    def test_to_dictArgs(self):
        """Test that to_dict() raises TypeError when called with an argument"""
        b_model = BaseModel()
        with self.assertRaises(TypeError):
            b_model.to_dict(None)

    def test_dict_datetime_attributes_are_strs(self):
        """tests if the dictionary attributes are strings"""
        b_model = BaseModel()
        b_model_dict = b_model.to_dict()
        self.assertIsInstance(b_model_dict["created_at"], str)
        self.assertIsInstance(b_model_dict["updated_at"], str)

    def test_of_dict_output(self):
        """tests the dictionary output"""
        dtFormat = datetime.today()
        b_model = BaseModel()
        b_model.id = "123456"
        b_model.created_at = b_model.updated_at = dtFormat
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dtFormat.isoformat(),
            'updated_at': dtFormat.isoformat()
        }
        self.assertDictEqual(b_model.to_dict(), tdict)
        
if __name__ == "__main__":
    unittest.main()
