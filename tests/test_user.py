#!/usr/bin/python3
"""Defines the unnittests cases for user_model"""

import os
import unittest
import models
from time import sleep

from datetime import datetime
from models.user import User
import models.user as user_doc


class Test_user_model_documentation(unittest.TestCase):
    """Tests the documentation on the models/user_model.py"""

    def test_user_doc(self):
        """tests the documantation on the user_model file"""
        self.assertGreater(len(user_doc.__doc__), 0)

    def test_user_model_save(self):
        """tests the documentation of the user_model file"""
        self.assertGreater(len(User.save.__doc__), 0)

    def test_user_model_toDict(self):
        """tests the documentation of the user_model file"""
        self.assertGreater(len(User.to_dict.__doc__), 0)

    def test_user_model_init(self):
        """tests the documentation of the user_model file"""
        self.assertGreater(len(User.__init__.__doc__), 0)

    def test_user_model_str(self):
        """tests the documentation of the user_model file"""
        self.assertGreater(len(User.__str__.__doc__), 0)

    def test_attribute_public(self):
        """tests if the attributes are public"""
        user_class = User()
        self.assertEqual(str, type(User().first_name))
        self.assertEqual(str, type(User().last_name))
        self.assertEqual(str, type(User().email))
        self.assertEqual(str, type(User().password))
        self.assertTrue(hasattr(user_class, 'first_name'))
        self.assertTrue(hasattr(user_class, 'last_name'))
        self.assertTrue(hasattr(user_class, 'password'))
        self.assertTrue(hasattr(user_class, 'email'))


class Test_user_model_initialization(unittest.TestCase):
    """tests the initialization method on user_model file"""

    def test_user_model_instances(self):
        """tests the instances of the user_model file"""
        user_class = User()
        self.assertTrue(type(user_class == User))

    def test_user_model_creationTime(self):
        """tests the created_at time of the user_model file"""
        user_class1 = User()
        sleep(0.02)
        user_class2 = User()
        self.assertGreater(user_class2.created_at, user_class1.created_at)

    def test_user_model_updatedTime(self):
        """tests the updated_at time of the user_model file"""
        user_class1 = User()
        sleep(0.03)
        user_class2 = User()
        self.assertGreater(user_class2.updated_at, user_class1.updated_at)

    def test_user_model_2_diff_id(self):
        """tests if 2 different id"""
        user_class1 = User()
        user_class2 = User()
        self.assertNotEqual(user_class1, user_class2)

    def test_user_model_uuid4(self):
        """tests if id is the type uf uuid4"""
        user_class1 = User()
        sleep(0.03)
        user_class2 = User()
        self.assertEqual(user_class1.id[14], '4')
        self.assertEqual(user_class2.id[14], '4')

    def test_unused_args(self):
        user_class = User(None)
        self.assertNotIn(None, user_class.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt_format = datetime.today()
        dt_iso_format = dt_format.isoformat()
        user_class = User(id="345", created_at=dt_iso_format,
                          updated_at=dt_iso_format)

        self.assertTrue(user_class.id == "345")
        self.assertTrue(user_class.created_at == dt_format)
        self.assertTrue(user_class.updated_at == dt_format)

    def test_of_None_kwargs_instantiation(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_user_model_initialization(self):
        """tests the initialization of the user attrinutes"""
        user_cl = User()
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")


class Test_user_model_str(unittest.TestCase):
    """tests the __str__ method on user_model file"""

    def test_user_model_id_string(self):
        """tests if the id is a string"""
        user_class = User()
        self.assertTrue(type(user_class.id) == str)

    def test_if_objStr(self):
        """tests if object is string"""
        user_class = User()
        user_class_result = f"{User}({id}){dict}"
        self.assertNotEqual(str(User), user_class_result)


class Test_user_model_save(unittest.TestCase):
    """Test cases for save method on user_model file"""

    @classmethod
    def setUpClass(cls):
        cls.backup_file_name = "tmp.json"
        cls.test_file_name = "file.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file_name):
            os.remove(cls.test_file_name)

    def test_user_model_save_dateTime(self):
        """tests for save method on user_model file"""
        user_class = User()
        sleep(0.03)
        updated_at1 = user_class.updated_at
        user_class.save()
        self.assertLess(updated_at1, user_class.updated_at)

    def test_bm_two_saves(self):
        """tests cases that save to base models"""
        user_class = User()
        first_updated_at = user_class.updated_at
        sleep(0.05)
        user_class.save()
        second_updated_at = user_class.updated_at
        self.assertTrue(first_updated_at < second_updated_at)
        sleep(0.05)
        user_class.save()
        self.assertTrue(second_updated_at < user_class.updated_at)

    def test_saveArgs(self):
        user_class = User()
        with self.assertRaises(TypeError):
            user_class.save(None)

    def test_save_updates_file(self):
        user_class = User()
        user_class.save()
        user_class_id = "User." + user_class.id
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertTrue(user_class_id in file_content)


class Test_user_model_to_dict(unittest.TestCase):
    """tests cases for to_dict on user_model file"""

    def test_user_model_to_dict(self):
        """test the to_dict method on the user_model"""
        user_class = User()
        self.assertTrue(isinstance(user_class.to_dict(), dict))

    def test_model_to_dict_keys(self):
        """tests the correct keys for the to_dict method on user_model file"""
        user_class = User()
        keys = ["id", "created_at", "updated_at", "__class__"]
        self.assertIn("id", user_class.to_dict())
        self.assertIn("created_at", user_class.to_dict())
        self.assertIn("updated_at", user_class.to_dict())
        self.assertIn("__class__", user_class.to_dict())

    def test_to_dictArgs(self):
        """Test that to_dict() raises TypeError when called with an argument"""
        user_class = User()
        with self.assertRaises(TypeError):
            user_class.to_dict(None)

    def test_dict_datetime_attributes_are_strs(self):
        """tests if the dictionary attributes are strings"""
        user_class = User()
        user_class_dict = user_class.to_dict()
        self.assertIsInstance(user_class_dict["created_at"], str)
        self.assertIsInstance(user_class_dict["updated_at"], str)

    def test_of_dict_output(self):
        """tests the dictionary output"""
        dtFormat = datetime.today()
        user_class = User()
        user_class.id = "123456"
        user_class.created_at = user_class.updated_at = dtFormat
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dtFormat.isoformat(),
            'updated_at': dtFormat.isoformat()
        }
        self.assertDictEqual(user_class.to_dict(), tdict)

    def test_user_model_assigned_attributes(self):
        """tests the assigned attrinutes on user file"""
        user_cl = User()
        User.email = "londy-ravi@gmail.com"
        User.password = "@password45"
        User.first_name = "Londeka"
        User.last_name = "Khotso"
        self.assertEqual(User.email, "londy-ravi@gmail.com")
        self.assertEqual(User.password, "@password45")
        self.assertEqual(User.first_name, "Londeka")
        self.assertEqual(User.last_name, "Khotso")


if __name__ == "__main__":
    unittest.main()
