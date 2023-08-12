#!/usr/bin/python3
"""Defines the unnittests cases for state"""

import os
import unittest
import models
from time import sleep

from datetime import datetime
from models.state import State
import models.state as bm_documentation


class Test_state_documentation(unittest.TestCase):
    """Tests the documentation on the models/state.py"""

    def test_bm_documentation(self):
        """tests the documantation on the state file"""
        self.assertGreater(len(bm_documentation.__doc__), 0)

    def test_state_save(self):
        """tests the documentation of the state file"""
        self.assertGreater(len(State.save.__doc__), 0)

    def test_state_toDict(self):
        """tests the documentation of the state file"""
        self.assertGreater(len(State.to_dict.__doc__), 0)

    def test_state_init(self):
        """tests the documentation of the state file"""
        self.assertGreater(len(State.__init__.__doc__), 0)

    def test_state_str(self):
        """tests the documentation of the state file"""
        self.assertGreater(len(State.__str__.__doc__), 0)

class Test_state_initialization(unittest.TestCase):
    """tests the initialization method on state file"""

    def test_state_instances(self):
        """tests the instances of the state file"""
        state_class = State()
        self.assertTrue(type(state_class == State))
    
    def test_state_creationTime(self):
        """tests the created_at time of the state file"""
        state_class1 = State()
        sleep(0.02)
        state_class2 = State()
        self.assertGreater(state_class2.created_at, state_class1.created_at)

    def test_state_updatedTime(self):
        """tests the updated_at time of the state file"""
        state_class1 = State()
        sleep(0.03)
        state_class2 = State()
        self.assertGreater(state_class2.updated_at, state_class1.updated_at)

    def test_state_2_diff_id(self):
        """tests if 2 different id"""
        state_class1 = State()
        state_class2 = State()
        self.assertNotEqual(state_class1, state_class2)

    def test_state_uuid4(self):
        """tests if id is the type uf uuid4"""
        state_class1 = State()
        sleep(0.03)
        state_class2 = State()
        self.assertEqual(state_class1.id[14], '4')
        self.assertEqual(state_class2.id[14], '4')

    def test_unused_args(self):
        state_class = State(None)
        self.assertNotIn(None, state_class.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt_format = datetime.today()
        dt_iso_format = dt_format.isoformat()
        state_class = State(id="345", created_at=dt_iso_format,
                       updated_at=dt_iso_format)
        
        self.assertTrue(state_class.id == "345")
        self.assertTrue(state_class.created_at == dt_format)
        self.assertTrue(state_class.updated_at == dt_format)

    def test_of_None_kwargs_instantiation(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

class Test_state_str(unittest.TestCase):
    """tests the __str__ method on state file"""

    def test_state_id_string(self):
        """tests if the id is a string"""
        state_class = State()
        self.assertTrue(type(state_class.id) == str)

    def test_if_objStr(self):
        """tests if object is string"""
        state_class = State()
        state_class_result = f"{State}({id}){dict}"
        self.assertNotEqual(str(State), state_class_result)

class Test_state_save(unittest.TestCase):
    """Test cases for save method on state file"""

    @classmethod
    def setUpClass(cls):
        cls.backup_file_name = "tmp.json"
        cls.test_file_name = "file.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file_name):
            os.remove(cls.test_file_name)

    def test_state_save_dateTime(self):
        """tests for save method on state file"""
        state_class = State()
        sleep(0.03)
        updated_at1 = state_class.updated_at
        state_class.save()
        self.assertLess(updated_at1, state_class.updated_at)

    def test_bm_two_saves(self):
        """tests cases that save to base models"""
        state_class = State()
        first_updated_at = state_class.updated_at
        sleep(0.05)
        state_class.save()
        second_updated_at = state_class.updated_at
        self.assertTrue(first_updated_at < second_updated_at)
        sleep(0.05)
        state_class.save()
        self.assertTrue(second_updated_at < state_class.updated_at)

    def test_saveArgs(self):
        state_class = State()
        with self.assertRaises(TypeError):
            state_class.save(None)

    def test_save_updates_file(self):
        state_class = State()
        state_class.save()
        state_class_id = "State." + state_class.id
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertTrue(state_class_id in file_content)

class Test_state_to_dict(unittest.TestCase):
    """tests cases for to_dict on state file"""

    def test_state_to_dict(self):
        """test the to_dict method on the Basemodel"""
        state_class = State()
        self.assertTrue(isinstance(state_class.to_dict(), dict))

    def test_model_to_dict_keys(self):
        """tests the correct keys for the to_dict method on Base_model file"""
        state_class = State()
        keys = ["id", "created_at", "updated_at", "__class__"]
        self.assertIn("id", state_class.to_dict())
        self.assertIn("created_at", state_class.to_dict())
        self.assertIn("updated_at", state_class.to_dict())
        self.assertIn("__class__", state_class.to_dict())

    def test_attribute_public(self):
        """tests if the attributes are public"""
        state_class = State()
        self.assertEqual(str, type(State().name))
        self.assertTrue(hasattr(state_class, 'name'))

    def test_to_dictArgs(self):
        """Test that to_dict() raises TypeError when called with an argument"""
        state_class = State()
        with self.assertRaises(TypeError):
            state_class.to_dict(None)

    def test_dict_datetime_attributes_are_strs(self):
        """tests if the dictionary attributes are strings"""
        state_class = State()
        state_class_dict = state_class.to_dict()
        self.assertIsInstance(state_class_dict["created_at"], str)
        self.assertIsInstance(state_class_dict["updated_at"], str)

    def test_of_dict_output(self):
        """tests the dictionary output"""
        dtFormat = datetime.today()
        state_class = State()
        state_class.id = "123456"
        state_class.created_at = state_class.updated_at = dtFormat
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dtFormat.isoformat(),
            'updated_at': dtFormat.isoformat()
        }
        self.assertDictEqual(state_class.to_dict(), tdict)
        
if __name__ == "__main__":
    unittest.main()
