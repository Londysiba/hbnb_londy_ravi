#!/usr/bin/python3
"""Defines the unnittests cases for city"""

import os
import unittest
import models
from time import sleep

from datetime import datetime
from models.city import City
import models.city as bm_documentation


class Test_city_documentation(unittest.TestCase):
    """Tests the documentation on the models/city.py"""

    def test_bm_documentation(self):
        """tests the documantation on the city file"""
        self.assertGreater(len(bm_documentation.__doc__), 0)

    def test_city_save(self):
        """tests the documentation of the city file"""
        self.assertGreater(len(City.save.__doc__), 0)

    def test_city_toDict(self):
        """tests the documentation of the city file"""
        self.assertGreater(len(City.to_dict.__doc__), 0)

    def test_city_init(self):
        """tests the documentation of the city file"""
        self.assertGreater(len(City.__init__.__doc__), 0)

    def test_city_str(self):
        """tests the documentation of the city file"""
        self.assertGreater(len(City.__str__.__doc__), 0)

class Test_city_initialization(unittest.TestCase):
    """tests the initialization method on city file"""

    def test_city_instances(self):
        """tests the instances of the city file"""
        city_class = City()
        self.assertTrue(type(city_class == City))
    
    def test_city_creationTime(self):
        """tests the created_at time of the city file"""
        city_class1 = City()
        sleep(0.02)
        city_class2 = City()
        self.assertGreater(city_class2.created_at, city_class1.created_at)

    def test_city_updatedTime(self):
        """tests the updated_at time of the city file"""
        city_class1 = City()
        sleep(0.03)
        city_class2 = City()
        self.assertGreater(city_class2.updated_at, city_class1.updated_at)

    def test_city_2_diff_id(self):
        """tests if 2 different id"""
        city_class1 = City()
        city_class2 = City()
        self.assertNotEqual(city_class1, city_class2)

    def test_city_uuid4(self):
        """tests if id is the type uf uuid4"""
        city_class1 = City()
        sleep(0.03)
        city_class2 = City()
        self.assertEqual(city_class1.id[14], '4')
        self.assertEqual(city_class2.id[14], '4')

    def test_unused_args(self):
        city_class = City(None)
        self.assertNotIn(None, city_class.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt_format = datetime.today()
        dt_iso_format = dt_format.isoformat()
        city_class = City(id="345", created_at=dt_iso_format,
                       updated_at=dt_iso_format)
        
        self.assertTrue(city_class.id == "345")
        self.assertTrue(city_class.created_at == dt_format)
        self.assertTrue(city_class.updated_at == dt_format)

    def test_of_None_kwargs_instantiation(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

class Test_city_str(unittest.TestCase):
    """tests the __str__ method on city file"""

    def test_city_id_string(self):
        """tests if the id is a string"""
        city_class = City()
        self.assertTrue(type(city_class.id) == str)

    def test_if_objStr(self):
        """tests if object is string"""
        city_class = City()
        city_class_result = f"{City}({id}){dict}"
        self.assertNotEqual(str(City), city_class_result)

class Test_city_save(unittest.TestCase):
    """Test cases for save method on city file"""

    @classmethod
    def setUpClass(cls):
        cls.backup_file_name = "tmp.json"
        cls.test_file_name = "file.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file_name):
            os.remove(cls.test_file_name)

    def test_city_save_dateTime(self):
        """tests for save method on city file"""
        city_class = City()
        sleep(0.03)
        updated_at1 = city_class.updated_at
        city_class.save()
        self.assertLess(updated_at1, city_class.updated_at)

    def test_bm_two_saves(self):
        """tests cases that save to base models"""
        city_class = City()
        first_updated_at = city_class.updated_at
        sleep(0.05)
        city_class.save()
        second_updated_at = city_class.updated_at
        self.assertTrue(first_updated_at < second_updated_at)
        sleep(0.05)
        city_class.save()
        self.assertTrue(second_updated_at < city_class.updated_at)

    def test_saveArgs(self):
        city_class = City()
        with self.assertRaises(TypeError):
            city_class.save(None)

    def test_save_updates_file(self):
        city_class = City()
        city_class.save()
        city_class_id = "City." + city_class.id
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertTrue(city_class_id in file_content)

class Test_city_to_dict(unittest.TestCase):
    """tests cases for to_dict on city file"""

    def test_city_to_dict(self):
        """test the to_dict method on the Basemodel"""
        city_class = City()
        self.assertTrue(isinstance(city_class.to_dict(), dict))

    def test_model_to_dict_keys(self):
        """tests the correct keys for the to_dict method on Base_model file"""
        city_class = City()
        keys = ["id", "created_at", "updated_at", "__class__"]
        self.assertIn("id", city_class.to_dict())
        self.assertIn("created_at", city_class.to_dict())
        self.assertIn("updated_at", city_class.to_dict())
        self.assertIn("__class__", city_class.to_dict())

    def test_attribute_public(self):
        """tests if the attributes are public"""
        city_class = City()
        self.assertEqual(str, type(City().name))
        self.assertTrue(hasattr(city_class, 'name'))
        self.assertEqual(str, type(City().state_id))
        self.assertTrue(hasattr(city_class, 'state_id'))

    def test_to_dictArgs(self):
        """Test that to_dict() raises TypeError when called with an argument"""
        city_class = City()
        with self.assertRaises(TypeError):
            city_class.to_dict(None)

    def test_dict_datetime_attributes_are_strs(self):
        """tests if the dictionary attributes are strings"""
        city_class = City()
        city_class_dict = city_class.to_dict()
        self.assertIsInstance(city_class_dict["created_at"], str)
        self.assertIsInstance(city_class_dict["updated_at"], str)

    def test_of_dict_output(self):
        """tests the dictionary output"""
        dtFormat = datetime.today()
        city_class = City()
        city_class.id = "123456"
        city_class.created_at = city_class.updated_at = dtFormat
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dtFormat.isoformat(),
            'updated_at': dtFormat.isoformat()
        }
        self.assertDictEqual(city_class.to_dict(), tdict)
        
if __name__ == "__main__":
    unittest.main()
