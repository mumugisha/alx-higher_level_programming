#!/usr/bin/python3

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

# Define a test class for the Base class
class TestBaseClass(unittest.TestCase):
    
    # Test case to ensure unique id assignment
    def test_id_assignment(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b12 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b12.id, 12)
        self.assertEqual(b3.id, 3)

    # Test case for the to_json_string method
    def test_to_json_string(self):
        Base._Base__nb_objects = 0
        # Test empty list
        temp = Base.to_json_string([])
        self.assertEqual(temp, "[]")
        # Test None
        temp = Base.to_json_string(None)
        self.assertEqual(temp, "[]")
        # Test with dictionary
        temp2 = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        temp = Base.to_json_string(temp2)
        self.assertEqual(temp, json.dumps(temp2))
        # Test list with empty dictionary
        temp = Base.to_json_string([{}])
        self.assertEqual(temp, json.dumps([{}]))
        # Test list with None
        temp = Base.to_json_string([None])
        self.assertEqual(temp, json.dumps([None]))
        # Test list with dictionary containing None
        temp = Base.to_json_string([{"a": None}])
        self.assertEqual(temp, json.dumps([{"a": None}]))

    # Test case for the from_json_string method
    def test_from_json_string(self):
        Base._Base__nb_objects = 0
        # Test empty list
        temp = Base.from_json_string(json.dumps([]))
        self.assertEqual(temp, [])
        # Test None
        temp = Base.from_json_string(None)
        self.assertEqual(temp, [])
        # Test with dictionary
        temp2 = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        json_str = json.dumps(temp2)
        temp = Base.from_json_string(json_str)
        self.assertEqual(temp, json.loads(json_str))

if __name__ == "__main__":
    unittest.main()
