#!/usr/bin/python3
""" Test Console """
import unittest
import os
import console
from unittest.mock import patch
from io import StringIO
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage


class TestConstructor(unittest.TestCase):
    """ Test Constructor """
    __classes_dict = {"BaseModel": BaseModel, "State": State, "State": State,
                      "City": City, "Amenity": Amenity,
                      "Place": Place, "Review": Review, "User": User}

    def test_help_method(self):
        """ Test Help """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(
                "Quit command to exit the program.", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual("EOF command to exit the program.",
                             f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(
                """Creates a new instance of BaseModel, saves it""",
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual("""Print the string representation of an instance
        based on the class name and id.""", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(
                """Delete an instance based on the class name and id.""",
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(
                """Print all string representation of all instances""",
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(
                """Updates an instance based on the class name and id""",
                f.getvalue()[:-1])

    def rest_file_storage(self):
        """ Test Storage """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        storage._FileStorage__objects = {}

    def create_new_objects(self):
        """ Create New """
        created_at = "2023-08-13T12:00:00"
        updated_at = "2023-08-13T13:30:00"

        user_data = {
            "id": "user_id_123",  # Set an appropriate unique ID here
            "email": "user@example.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "created_at": created_at,
            "updated_at": updated_at
        }
        u = User(**user_data)
        storage.new(u)
        amenity_data = {
            "id": "amenity_id_456",  # Set an appropriate unique ID here
            "name": "Wi-Fi",
            "created_at": created_at,
            "updated_at": updated_at
        }
        a = Amenity(**amenity_data)
        storage.new(a)
        state_data = {
            "id": "state_id_789",  # Set an appropriate unique ID here
            "name": "California",
            "created_at": created_at,
            "updated_at": updated_at
        }
        s = State(**state_data)
        storage.new(s)
        city_data = {
            "id": "city_id_101",  # Set an appropriate unique ID here
            "state_id": s.id,
            "name": "San Francisco",
            "created_at": created_at,
            "updated_at": updated_at
        }
        c = City(**city_data)
        storage.new(c)
        place_data = {
            "id": "place_id_111",  # Set an appropriate unique ID here
            "city_id": c.id,
            "user_id": u.id,
            "name": "Cozy Cottage",
            "description": "A lovely cottage in the heart of the city.",
            "number_rooms": 2,
            "number_bathrooms": 1,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "created_at": created_at,
            "updated_at": updated_at
        }
        p = Place(**place_data)
        storage.new(p)
        review_data = {
            "id": "review_id_222",  # Set an appropriate unique ID here
            "place_id": p.id,
            "user_id": u.id,
            "text": "Had a great time staying here!",
            "created_at": created_at,
            "updated_at": updated_at
        }
        r = Review(**review_data)
        storage.new(r)
        b = BaseModel(id="base_id_333", created_at=created_at,
                      updated_at=updated_at)
        storage.new(b)
        storage.save()  # Save all the created objects

    def test_create(self):
        """ Test Create """
        self.rest_file_storage()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])

        for k in self.__classes_dict.keys():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {k}")
                self.assertTrue(f"{k}."+f.getvalue()
                                [:-1] in storage.all().keys())
                self.assertIsInstance(storage.all().get(
                    f"{k}."+f.getvalue()[:-1]), eval(k))
        self.assertTrue(os.path.isfile("file.json"))

    def test_create_key_values(self):
        """ Test Create Key """
        self.rest_file_storage()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="t"e_st"')
            self.assertTrue("City."+f.getvalue()
                            [:-1] in storage.all().keys())
            self.assertIsInstance(storage.all().get(
                f"City."+f.getvalue()[:-1]), City)
            self.assertIn("'name': 't\"e_st'", output)

    def test_docstrings(self):
        """ Test Docstrings """
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.strip_clean.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)
        self.assertIsNotNone(console.__doc__)

    def test_show(self):
        """ Test Show """
        self.rest_file_storage()
        self.create_new_objects()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual("** instance id missing **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 3212133")
            self.assertEqual("** no instance found **", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User user_id_123")
            self.assertEqual(
                storage.all()["User.user_id_123"].__str__(), f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Amenity amenity_id_456")
            self.assertEqual(
                storage.all()["Amenity.amenity_id_456"].__str__(),
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State state_id_789")
            self.assertEqual(
                storage.all()["State.state_id_789"].__str__(),
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show City city_id_101")
            self.assertEqual(
                storage.all()["City.city_id_101"].__str__(), f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Place place_id_111")
            self.assertEqual(
                storage.all()["Place.place_id_111"].__str__(),
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Review review_id_222")
            self.assertEqual(
                storage.all()["Review.review_id_222"].__str__(),
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel base_id_333")
            self.assertEqual(
                storage.all()["BaseModel.base_id_333"].__str__(),
                f.getvalue()[:-1])

    def test_destroy(self):
        """ Test Destroy """
        self.rest_file_storage()
        self.create_new_objects()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual("** instance id missing **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 3212133")
            self.assertEqual("** no instance found **", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User user_id_123")
            self.assertEqual("", f.getvalue()[:-1])
            self.assertFalse("User.user_id_123" in storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Amenity amenity_id_456")
            self.assertEqual("", f.getvalue()[:-1])
            self.assertFalse("Amenity.amenity_id_456" in storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy State state_id_789")
            self.assertEqual("", f.getvalue()[:-1])
            self.assertFalse("State.state_id_789" in storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy City city_id_101")
            self.assertEqual("", f.getvalue()[:-1])
            self.assertFalse("City.city_id_101" in storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Place place_id_111")
            self.assertFalse("Place.place_id_111" in storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Review review_id_222")
            self.assertEqual("", f.getvalue()[:-1])
            self.assertFalse("Review.review_id_222" in storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel base_id_333")
            self.assertEqual("", f.getvalue()[:-1])
            self.assertFalse("BaseModel.base_id_333" in storage.all().keys())

        def test_count(self):
            """ Test Count """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("count")
                self.assertEqual("** class name missing **", f.getvalue()[:-1])
            for k in self.__classes_dict.keys():
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"count {k}")
                    expected_count = len([obj for obj in storage.all(
                    ).values() if isinstance(obj, self.__classes_dict[k])])
                    self.assertEqual(str(expected_count), f.getvalue()[:-1])
