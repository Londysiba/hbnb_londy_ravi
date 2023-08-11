#!/usr/bin/python3
"""Defines the unnittests cases for base_model"""

import unittest
from models.base_model import BaseModel
import models.base_model as bm_documentation
from time import sleep

class Test_basemodel_documentation(unittest.TestCase):
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

    def test_base_model_id_string(self):
        """tests if the id is a string"""
        b_model = BaseModel()
        self.assertTrue(type(b_model.id) == str)

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

if __name__ == "__main__":
    unittest.main()




