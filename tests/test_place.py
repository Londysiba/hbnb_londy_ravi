import os
import unittest
import models
from time import sleep

from datetime import datetime
from models.place import Place
import models.place as place_doc


class Test_place_model_documentation(unittest.TestCase):
    """Tests the documentation on the models/place_model.py"""

    def test_place_doc(self):
        """tests the documantation on the place_model file"""
        self.assertGreater(len(Place.__doc__), 0)

    def test_place_model_save(self):
        """tests the documentation of the place_model file"""
        self.assertGreater(len(Place.save.__doc__), 0)

    def test_place_model_toDict(self):
        """tests the documentation of the place_model file"""
        self.assertGreater(len(Place.to_dict.__doc__), 0)

    def test_place_model_init(self):
        """tests the documentation of the place_model file"""
        self.assertGreater(len(Place.__init__.__doc__), 0)

    def test_place_model_str(self):
        """tests the documentation of the place_model file"""
        self.assertGreater(len(Place.__str__.__doc__), 0)

    def test_attribute_public(self):
        """tests if the attributes are public"""
        place_class = Place()
        self.assertEqual(str, type(Place().city_id))
        self.assertEqual(str, type(Place().user_id))
        self.assertEqual(str, type(Place().description))
        self.assertEqual(int, type(Place().number_rooms))
        self.assertEqual(int, type(Place().number_bathrooms))
        self.assertEqual(int, type(Place().max_guest))
        self.assertEqual(int, type(Place().price_by_night))
        self.assertEqual(float, type(Place().latitude))
        self.assertEqual(float, type(Place().longitude))
        self.assertEqual(list, type(Place().amenity_ids))

        self.assertTrue(hasattr(place_class, 'city_id'))
        self.assertTrue(hasattr(place_class, 'user_id'))
        self.assertTrue(hasattr(place_class, 'description'))
        self.assertTrue(hasattr(place_class, 'number_rooms'))
        self.assertTrue(hasattr(place_class, 'number_bathrooms'))
        self.assertTrue(hasattr(place_class, 'max_guest'))


class Test_place_model_initialization(unittest.TestCase):
    """tests the initialization method on place_model file"""

    def test_place_model_instances(self):
        """tests the instances of the place_model file"""
        place_class = Place()
        self.assertTrue(type(place_class == Place))

    def test_place_model_creationTime(self):
        """tests the created_at time of the place_model file"""
        place_class1 = Place()
        sleep(0.02)
        place_class2 = Place()
        self.assertGreater(place_class2.created_at, place_class1.created_at)

    def test_place_model_updatedTime(self):
        """tests the updated_at time of the place_model file"""
        place_class1 = Place()
        sleep(0.03)
        place_class2 = Place()
        self.assertGreater(place_class2.updated_at, place_class1.updated_at)

    def test_place_model_2_diff_id(self):
        """tests if 2 different id"""
        place_class1 = Place()
        place_class2 = Place()
        self.assertNotEqual(place_class1, place_class2)

    def test_place_model_uuid4(self):
        """tests if id is the type uf uuid4"""
        place_class1 = Place()
        sleep(0.03)
        place_class2 = Place()
        self.assertEqual(place_class1.id[14], '4')
        self.assertEqual(place_class2.id[14], '4')

    def test_unused_args(self):
        place_class = Place(None)
        self.assertNotIn(None, place_class.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt_format = datetime.today()
        dt_iso_format = dt_format.isoformat()
        place_class = Place(id="345", created_at=dt_iso_format,
                            updated_at=dt_iso_format)

        self.assertTrue(place_class.id == "345")
        self.assertTrue(place_class.created_at == dt_format)
        self.assertTrue(place_class.updated_at == dt_format)

    def test_of_None_kwargs_instantiation(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_place_model_initialization(self):
        """tests the initialization of the place attributes"""
        place_cl = Place()
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.description, "")
        self.assertGreaterEqual(Place.number_bathrooms, 0)
        self.assertGreaterEqual(Place.number_rooms, 0)
        self.assertGreaterEqual(Place.max_guest, 0)
        self.assertGreaterEqual(Place.price_by_night, 0)
        self.assertGreaterEqual(Place.latitude, 0)
        self.assertGreaterEqual(Place.longitude, 0)
        self.assertEqual(Place.amenity_ids, [])


class Test_place_model_str(unittest.TestCase):
    """tests the __str__ method on place_model file"""

    def test_place_model_id_string(self):
        """tests if the id is a string"""
        place_class = Place()
        self.assertTrue(type(place_class.id) == str)

    def test_if_objStr(self):
        """tests if object is string"""
        place_class = Place()
        place_class_result = f"{Place}({id}){dict}"
        self.assertNotEqual(str(Place), place_class_result)


class Test_place_model_save(unittest.TestCase):
    """Test cases for save method on place_model file"""

    @classmethod
    def setUpClass(cls):
        cls.backup_file_name = "tmp.json"
        cls.test_file_name = "file.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file_name):
            os.remove(cls.test_file_name)

    def test_place_model_save_dateTime(self):
        """tests for save method on place_model file"""
        place_class = Place()
        sleep(0.03)
        updated_at1 = place_class.updated_at
        place_class.save()
        self.assertLess(updated_at1, place_class.updated_at)

    def test_bm_two_saves(self):
        """tests cases that save to base models"""
        place_class = Place()
        first_updated_at = place_class.updated_at
        sleep(0.05)
        place_class.save()
        second_updated_at = place_class.updated_at
        self.assertTrue(first_updated_at < second_updated_at)
        sleep(0.05)
        place_class.save()
        self.assertTrue(second_updated_at < place_class.updated_at)

    def test_saveArgs(self):
        place_class = Place()
        with self.assertRaises(TypeError):
            place_class.save(None)

    def test_save_updates_file(self):
        place_class = Place()
        place_class.save()
        place_class_id = "Place." + place_class.id
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertTrue(place_class_id in file_content)


class Test_place_model_to_dict(unittest.TestCase):
    """tests cases for to_dict on place_model file"""

    def test_place_model_to_dict(self):
        """test the to_dict method on the place_model"""
        place_class = Place()
        self.assertTrue(isinstance(place_class.to_dict(), dict))

    def test_model_to_dict_keys(self):
        """tests the correct keys for the to_dict method on place_model file"""
        place_class = Place()
        keys = ["id", "created_at", "updated_at", "__class__"]
        self.assertIn("id", place_class.to_dict())
        self.assertIn("created_at", place_class.to_dict())
        self.assertIn("updated_at", place_class.to_dict())
        self.assertIn("__class__", place_class.to_dict())

    def test_to_dictArgs(self):
        """Test that to_dict() raises TypeError when called with an argument"""
        place_class = Place()
        with self.assertRaises(TypeError):
            place_class.to_dict(None)

    def test_dict_datetime_attributes_are_strs(self):
        """tests if the dictionary attributes are strings"""
        place_class = Place()
        place_class_dict = place_class.to_dict()
        self.assertIsInstance(place_class_dict["created_at"], str)
        self.assertIsInstance(place_class_dict["updated_at"], str)

    def test_of_dict_output(self):
        """tests the dictionary output"""
        dtFormat = datetime.today()
        place_class = Place()
        place_class.id = "123456"
        place_class.created_at = place_class.updated_at = dtFormat
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dtFormat.isoformat(),
            'updated_at': dtFormat.isoformat()
        }
        self.assertDictEqual(place_class.to_dict(), tdict)

    def test_place_model_assigned_attributes(self):
        """tests the assigned attrinutes on place file"""
        place_cl = Place()
        Place.city_id = "Durban"
        Place.user_id = "8398470248930"
        Place.description = "Londeka-khotso"
        Place.number_rooms = "3"
        Place.number_bathrooms = "2"
        Place.max_guest = "3"
        Place.price_by_night = "R1600"
        Place.latitude = "0"
        Place.longitude = "0"
        Place.amenity_ids = "[]"

        self.assertEqual(Place.city_id, "Durban")
        self.assertEqual(Place.user_id, "8398470248930")
        self.assertEqual(Place.description, "Londeka-khotso")
        self.assertEqual(Place.number_bathrooms, "2")
        self.assertEqual(Place.number_rooms, "3")
        self.assertEqual(Place.max_guest, "3")
        self.assertEqual(Place.price_by_night, "R1600")
        self.assertEqual(Place.latitude, "0")
        self.assertEqual(Place.longitude, "0")
        self.assertEqual(Place.amenity_ids, "[]")


if __name__ == "__main__":
    unittest.main()
