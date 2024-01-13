#!/usr/bin/python3
import unittest
import pep8
from models import base_model
from models.base_model import BaseModel
import inspect
import datetime


class TestPEP8Compliance(unittest.TestCase):
    def test_pep8_compliance(self):
        """Specify the Python files or directories to check"""
        files_to_check = ['models/base_model.py']

        # Create a StyleGuide instance
        style_guide = pep8.StyleGuide()

        # Check the specified files or directories for PEP 8 compliance
        report = style_guide.check_files(files_to_check)

        # Assert that there are no PEP 8 violations
        self.assertEqual(report.total_errors, 0,
                         f"PEP 8 violations found:\n{report.messages}")

    def test_pep8(self):
        # Specify the Python files or directories to check
        files_to_check = ['tests/test_models/test_base_model.py']

        # Create a StyleGuide instance
        style_guide = pep8.StyleGuide()

        # Check the specified files or directories for PEP 8 compliance
        report = style_guide.check_files(files_to_check)

        # Assert that there are no PEP 8 violations
        self.assertEqual(report.total_errors, 0,
                         f"PEP 8 violations found:\n{report.messages}")

    def test_doc(self):
        """test case for docstrings"""
        base_mod_doc = base_model.__doc__
        self.assertTrue(len(base_mod_doc) > 0, "Please Include a Docstring")

    def test_base_model_class_doc(self):
        """test case for docstrings"""
        base_mod_doc = BaseModel.__doc__
        self.assertTrue(len(base_mod_doc) > 0, "Please Include a Docstring")

    def test_class_methods(self):
        """test all the functions doc in base model"""
        class_methods = inspect.getmembers(BaseModel, inspect.isfunction)
        for func in class_methods:
            self.assertTrue(len(func[1].__doc__) > 0)


class TestBaseModel(unittest.TestCase):
    """test for the BaseModel class"""

    def setUp(self) -> None:
        """set up the BaseModel"""
        self.base_model = BaseModel()

    def tearDown(self) -> None:
        self.base_model = None

    def test_init__(self):
        base = self.base_model
        """test for the init method"""
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(hasattr(base, 'created_at'))
        self.assertTrue((hasattr(base, 'updated_at')))
        self.assertTrue(hasattr(base, 'id'))
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime.datetime,
                              "Invalid date")
        self.assertIsInstance(base.updated_at, datetime.datetime,
                              "Invalid date")

    def test_string_repr(self):
        """test for the string repr of object"""
        str_repr = str(self.base_model)
        self.assertIn("[BaseModel]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn("created_at", str_repr)
        self.assertIn("updated_at", str_repr)

    def test_save_method(self):
        """test for the save method"""
        base = self.base_model
        initial_update = base.updated_at
        # simulate a change
        base.email = "kelly@gmail.com"
        # call save method
        base.save()
        # check if the updated_at changed
        self.assertNotEqual(base.updated_at, initial_update,
                            "save method did not update updated at")

    def test_to_dict(self):
        """test for the to_dict method"""
        base = self.base_model
        obj_dict = base.to_dict()

        self.assertIsInstance(obj_dict, dict,
                              "object not an instance of dictionary")
        self.assertIn('__class__', obj_dict,
                      "__class__ not in dic")

        self.assertIn('created_at', obj_dict,
                      "Missing created_at key in to_dict result")
        self.assertIn('updated_at', obj_dict,
                      "Missing updated_at key in to_dict resul")
        self.assertIsInstance('created_at', str,
                              "created_at not an instance of str")
        self.assertIsInstance('updated_at', str,
                              "updated_at not an instance of str")
