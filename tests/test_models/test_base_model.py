#!/usr/bin/python3
"""
Unittest for base module
"""
import io
import unittest
import os
import models
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_BaseModel(unittest.TestCase):
    """ Test for
    Base_Model Class """

    def setUp(self):
        """set up the
        test for testing bae models"""
        FileStorage._FileStorage__file_path = "file.json"

    def test_noarg(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_None(self):
        Bmodel = BaseModel(None)
        self.assertNotIn(None, Bmodel.__dict__.values())

    def test_publicid(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_public_createat(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_public_updateat(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_all_storage_obj(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_all_str(self):
        date_time = datetime.today()
        date_repr = repr(date_time)
        Bmodel = BaseModel()
        Bmodel.id = "456789123"
        Bmodel.created_at = Bmodel.updated_at = date_time
        Bmodel_str = Bmodel.__str__()
        self.assertIn("[BaseModel] (456789123)", Bmodel_str)
        self.assertIn("'id': '456789123'", Bmodel_str)
        self.assertIn("'created_at': " + date_repr, Bmodel_str)
        self.assertIn("'updated_at': " + date_repr, Bmodel_str)

    def test_two_models(self):
        Bmodel1 = BaseModel()
        Bmodel2 = BaseModel()
        self.assertNotEqual(Bmodel1.id, Bmodel2.id)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        date_time = datetime.today()
        date_iso = date_time.isoformat()
        Bmodel = BaseModel(id="123", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(Bmodel.id, "123")
        self.assertEqual(Bmodel.created_at, date_time)
        self.assertEqual(Bmodel.updated_at, date_time)


if __name__ == "__main__":
    unittest.main()
