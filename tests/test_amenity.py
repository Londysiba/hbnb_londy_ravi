#!/usr/bin/python3
"""Defines the unnittests cases for amenity"""

import os
import unittest
import models
from time import sleep

from datetime import datetime
from models.amenity import Amenity
import models.amenity as bm_documentation


class Test_amenity_documentation(unittest.TestCase):
    """Tests the documentation on the models/amenity.py"""

    def test_bm_documentation(self):
        """tests the documantation on the amenity file"""
        self.assertGreater(len(bm_documentation.__doc__), 0)

    def test_amenity_save(self):
        """tests the documentation of the amenity file"""
        self.assertGreater(len(Amenity.save.__doc__), 0)

    def test_amenity_toDict(self):
        """tests the documentation of the amenity file"""
        self.assertGreater(len(Amenity.to_dict.__doc__), 0)

    def test_amenity_init(self):
        """tests the documentation of the amenity file"""
        self.assertGreater(len(Amenity.__init__.__doc__), 0)

    def test_amenity_str(self):
        """tests the documentation of the amenity file"""
        self.assertGreater(len(Amenity.__str__.__doc__), 0)


class Test_amenity_initialization(unittest.TestCase):
    """tests the initialization method on amenity file"""

    def test_amenity_instances(self):
        """tests the instances of the amenity file"""
        amenity_class = Amenity()
        self.assertTrue(type(amenity_class == Amenity))

    def test_amenity_creationTime(self):
        """tests the created_at time of the amenity file"""
        amenity_class1 = Amenity()
        sleep(0.02)
        amenity_class2 = Amenity()
        self.assertGreater(amenity_class2.created_at,
                           amenity_class1.created_at)

    def test_amenity_updatedTime(self):
        """tests the updated_at time of the amenity file"""
        amenity_class1 = Amenity()
        sleep(0.03)
        amenity_class2 = Amenity()
        self.assertGreater(amenity_class2.updated_at,
                           amenity_class1.updated_at)

    def test_amenity_2_diff_id(self):
        """tests if 2 different id"""
        amenity_class1 = Amenity()
        amenity_class2 = Amenity()
        self.assertNotEqual(amenity_class1, amenity_class2)

    def test_amenity_uuid4(self):
        """tests if id is the type uf uuid4"""
        amenity_class1 = Amenity()
        sleep(0.03)
        amenity_class2 = Amenity()
        self.assertEqual(amenity_class1.id[14], '4')
        self.assertEqual(amenity_class2.id[14], '4')

    def test_unused_args(self):
        amenity_class = Amenity(None)
        self.assertNotIn(None, amenity_class.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt_format = datetime.today()
        dt_iso_format = dt_format.isoformat()
        amenity_class = Amenity(id="345",
                                created_at=dt_iso_format,
                                updated_at=dt_iso_format)

        self.assertTrue(amenity_class.id == "345")
        self.assertTrue(amenity_class.created_at == dt_format)
        self.assertTrue(amenity_class.updated_at == dt_format)

    def test_of_None_kwargs_instantiation(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class Test_amenity_str(unittest.TestCase):
    """tests the __str__ method on amenity file"""

    def test_amenity_id_string(self):
        """tests if the id is a string"""
        amenity_class = Amenity()
        self.assertTrue(type(amenity_class.id) == str)

    def test_if_objStr(self):
        """tests if object is string"""
        amenity_class = Amenity()
        amenity_class_result = f"{Amenity}({id}){dict}"
        self.assertNotEqual(str(Amenity), amenity_class_result)


class Test_amenity_save(unittest.TestCase):
    """Test cases for save method on amenity file"""

    @classmethod
    def setUpClass(cls):
        cls.backup_file_name = "tmp.json"
        cls.test_file_name = "file.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file_name):
            os.remove(cls.test_file_name)

    def test_amenity_save_dateTime(self):
        """tests for save method on amenity file"""
        amenity_class = Amenity()
        sleep(0.03)
        updated_at1 = amenity_class.updated_at
        amenity_class.save()
        self.assertLess(updated_at1, amenity_class.updated_at)

    def test_bm_two_saves(self):
        """tests cases that save to base models"""
        amenity_class = Amenity()
        first_updated_at = amenity_class.updated_at
        sleep(0.05)
        amenity_class.save()
        second_updated_at = amenity_class.updated_at
        self.assertTrue(first_updated_at < second_updated_at)
        sleep(0.05)
        amenity_class.save()
        self.assertTrue(second_updated_at < amenity_class.updated_at)

    def test_saveArgs(self):
        amenity_class = Amenity()
        with self.assertRaises(TypeError):
            amenity_class.save(None)

    def test_save_updates_file(self):
        amenity_class = Amenity()
        amenity_class.save()
        amenity_class_id = "Amenity." + amenity_class.id
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertTrue(amenity_class_id in file_content)


class Test_amenity_to_dict(unittest.TestCase):
    """tests cases for to_dict on amenity file"""

    def test_amenity_to_dict(self):
        """test the to_dict method on the Basemodel"""
        amenity_class = Amenity()
        self.assertTrue(isinstance(amenity_class.to_dict(), dict))

    def test_model_to_dict_keys(self):
        """tests the correct keys for the to_dict method on Base_model file"""
        amenity_class = Amenity()
        keys = ["id", "created_at", "updated_at", "__class__"]
        self.assertIn("id", amenity_class.to_dict())
        self.assertIn("created_at", amenity_class.to_dict())
        self.assertIn("updated_at", amenity_class.to_dict())
        self.assertIn("__class__", amenity_class.to_dict())

    def test_attribute_public(self):
        """tests if the attributes are public"""
        amenity_class = Amenity()
        self.assertEqual(str, type(Amenity().name))
        self.assertTrue(hasattr(amenity_class, 'name'))

    def test_to_dictArgs(self):
        """Test that to_dict() raises TypeError when called with an argument"""
        amenity_class = Amenity()
        with self.assertRaises(TypeError):
            amenity_class.to_dict(None)

    def test_dict_datetime_attributes_are_strs(self):
        """tests if the dictionary attributes are strings"""
        amenity_class = Amenity()
        amenity_class_dict = amenity_class.to_dict()
        self.assertIsInstance(amenity_class_dict["created_at"], str)
        self.assertIsInstance(amenity_class_dict["updated_at"], str)

    def test_of_dict_output(self):
        """tests the dictionary output"""
        dtFormat = datetime.today()
        amenity_class = Amenity()
        amenity_class.id = "123456"
        amenity_class.created_at = amenity_class.updated_at = dtFormat
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dtFormat.isoformat(),
            'updated_at': dtFormat.isoformat()
        }
        self.assertDictEqual(amenity_class.to_dict(), tdict)


if __name__ == "__main__":
    unittest.main()
