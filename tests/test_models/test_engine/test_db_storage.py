#!/usr/bin/python3
""" DBStorage """
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") == "db",
    "this work only in db storage mode"
)
class test_DBStorage(unittest.TestCase):
    """ Test DBStorage """

    def setUp(self):
        """ Set Up DB"""
        self.storage = DBStorage()

    def tearDown(self):
        """ Remove Storage """
        del self.storage

    def test_pep8_DBStorage(self):
        """ Test pep8 """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_all(self):
        """ Test All """
        storage = DBStorage()
        storage.reload()
        obj = storage.all()
        self.assertEqual(type(obj), dict)

    def test_new(self):
        """ Test new """
        storage = DBStorage()
        storage.reload()
        obj = storage.all()
        obj = obj.copy()
        new = BaseModel()
        storage.new(new)
        storage.save()
        key = new.__class__.__name__ + "." + str(new.id)
        self.assertIsNotNone(obj[key])

    def test_reload(self):
        """ Test Reload """
        storage = DBStorage()
        storage.reload()
        obj = storage.all()
        self.assertEqual(type(obj), dict)
