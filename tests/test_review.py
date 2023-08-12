import os
import unittest
import models
from time import sleep

from datetime import datetime
from models.review import Review
import models.review as review_doc


class Test_review_model_documentation(unittest.TestCase):
    """Tests the documentation on the models/review_model.py"""

    def test_review_doc(self):
        """tests the documantation on the review_model file"""
        self.assertGreater(len(review_doc.__doc__), 0)

    def test_review_model_save(self):
        """tests the documentation of the review_model file"""
        self.assertGreater(len(Review.save.__doc__), 0)

    def test_review_model_toDict(self):
        """tests the documentation of the review_model file"""
        self.assertGreater(len(Review.to_dict.__doc__), 0)

    def test_review_model_init(self):
        """tests the documentation of the review_model file"""
        self.assertGreater(len(Review.__init__.__doc__), 0)

    def test_review_model_str(self):
        """tests the documentation of the review_model file"""
        self.assertGreater(len(Review.__str__.__doc__), 0)

    def test_attribute_public(self):
        """tests if the attributes are public"""
        review_class = Review()
        self.assertEqual(str, type(Review().place_id))
        self.assertEqual(str, type(Review().user_id))
        self.assertEqual(str, type(Review().text))

        self.assertTrue(hasattr(review_class, 'place_id'))
        self.assertTrue(hasattr(review_class, 'user_id'))
        self.assertTrue(hasattr(review_class, 'text'))


class Test_review_model_initialization(unittest.TestCase):
    """tests the initialization method on review_model file"""

    def test_review_model_instances(self):
        """tests the instances of the review_model file"""
        review_class = Review()
        self.assertTrue(type(review_class == Review))

    def test_review_model_creationTime(self):
        """tests the created_at time of the review_model file"""
        review_class1 = Review()
        sleep(0.02)
        review_class2 = Review()
        self.assertGreater(review_class2.created_at, review_class1.created_at)

    def test_review_model_updatedTime(self):
        """tests the updated_at time of the review_model file"""
        review_class1 = Review()
        sleep(0.03)
        review_class2 = Review()
        self.assertGreater(review_class2.updated_at, review_class1.updated_at)

    def test_review_model_2_diff_id(self):
        """tests if 2 different id"""
        review_class1 = Review()
        review_class2 = Review()
        self.assertNotEqual(review_class1, review_class2)

    def test_review_model_uuid4(self):
        """tests if id is the type uf uuid4"""
        review_class1 = Review()
        sleep(0.03)
        review_class2 = Review()
        self.assertEqual(review_class1.id[14], '4')
        self.assertEqual(review_class2.id[14], '4')

    def test_unused_args(self):
        review_class = Review(None)
        self.assertNotIn(None, review_class.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt_format = datetime.today()
        dt_iso_format = dt_format.isoformat()
        review_class = Review(id="345", created_at=dt_iso_format,
                              updated_at=dt_iso_format)

        self.assertTrue(review_class.id == "345")
        self.assertTrue(review_class.created_at == dt_format)
        self.assertTrue(review_class.updated_at == dt_format)

    def test_of_None_kwargs_instantiation(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_review_model_initialization(self):
        """tests the initialization of the review attrinutes"""
        review_cl = Review()
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")


class Test_review_model_str(unittest.TestCase):
    """tests the __str__ method on review_model file"""

    def test_review_model_id_string(self):
        """tests if the id is a string"""
        review_class = Review()
        self.assertTrue(type(review_class.id) == str)

    def test_if_objStr(self):
        """tests if object is string"""
        review_class = Review()
        review_class_result = f"{Review}({id}){dict}"
        self.assertNotEqual(str(Review), review_class_result)


class Test_review_model_save(unittest.TestCase):
    """Test cases for save method on review_model file"""

    @classmethod
    def setUpClass(cls):
        cls.backup_file_name = "tmp.json"
        cls.test_file_name = "file.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file_name):
            os.remove(cls.test_file_name)

    def test_review_model_save_dateTime(self):
        """tests for save method on review_model file"""
        review_class = Review()
        sleep(0.03)
        updated_at1 = review_class.updated_at
        review_class.save()
        self.assertLess(updated_at1, review_class.updated_at)

    def test_bm_two_saves(self):
        """tests cases that save to base models"""
        review_class = Review()
        first_updated_at = review_class.updated_at
        sleep(0.05)
        review_class.save()
        second_updated_at = review_class.updated_at
        self.assertTrue(first_updated_at < second_updated_at)
        sleep(0.05)
        review_class.save()
        self.assertTrue(second_updated_at < review_class.updated_at)

    def test_saveArgs(self):
        review_class = Review()
        with self.assertRaises(TypeError):
            review_class.save(None)

    def test_save_updates_file(self):
        review_class = Review()
        review_class.save()
        review_class_id = "Review." + review_class.id
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertTrue(review_class_id in file_content)


class Test_review_model_to_dict(unittest.TestCase):
    """tests cases for to_dict on review_model file"""

    def test_review_model_to_dict(self):
        """test the to_dict method on the review_model"""
        review_class = Review()
        self.assertTrue(isinstance(review_class.to_dict(), dict))

    def test_model_to_dict_keys(self):
        """tests the correct keys for the
        to_dict method on review_model file"""
        review_class = Review()
        keys = ["id", "created_at", "updated_at", "__class__"]
        self.assertIn("id", review_class.to_dict())
        self.assertIn("created_at", review_class.to_dict())
        self.assertIn("updated_at", review_class.to_dict())
        self.assertIn("__class__", review_class.to_dict())

    def test_to_dictArgs(self):
        """Test that to_dict() raises TypeError when called with an argument"""
        review_class = Review()
        with self.assertRaises(TypeError):
            review_class.to_dict(None)

    def test_dict_datetime_attributes_are_strs(self):
        """tests if the dictionary attributes are strings"""
        review_class = Review()
        review_class_dict = review_class.to_dict()
        self.assertIsInstance(review_class_dict["created_at"], str)
        self.assertIsInstance(review_class_dict["updated_at"], str)

    def test_of_dict_output(self):
        """tests the dictionary output"""
        dtFormat = datetime.today()
        review_class = Review()
        review_class.id = "123456"
        review_class.created_at = review_class.updated_at = dtFormat
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dtFormat.isoformat(),
            'updated_at': dtFormat.isoformat()
        }
        self.assertDictEqual(review_class.to_dict(), tdict)

    def test_review_model_assigned_attributes(self):
        """tests the assigned attrinutes on review file"""
        review_cl = Review()
        Review.place_id = "Durban"
        Review.user_id = "8398470248930"
        Review.text = "Londeka-khotso"

        self.assertEqual(Review.place_id, "Durban")
        self.assertEqual(Review.user_id, "8398470248930")
        self.assertEqual(Review.text, "Londeka-khotso")


if __name__ == "__main__":
    unittest.main()
