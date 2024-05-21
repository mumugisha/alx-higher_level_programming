#!/usr/bin/python3

# Importing necessary modules
import unittest
import json
import io
import sys

# Importing classes from models module
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square

# Test class for Square
class TestSquare(unittest.TestCase):
    # Test case for initializing Square instances
    def test_init(self):
        Base._Base__nb_objects = 0
        x = Square(10)
        y = Square(10)
        self.assertEqual(x.id, 1)
        self.assertEqual(y.id, 2)

    # Test case for checking attributes of Square instances
    def test_attrs(self):
        Base._Base__nb_objects = 0
        x = Square(10, 10, 10, 15)
        self.assertEqual(x.size, 10)
        self.assertEqual(x.x, 10)
        self.assertEqual(x.y, 10)
        self.assertEqual(x.id, 15)
        x = Square(56444, 500, 90000, 240000)
        self.assertEqual(x.size, 56444)
        self.assertEqual(x.x, 500)
        self.assertEqual(x.y, 90000)
        self.assertEqual(x.id, 240000)

    # Test case for checking type validation of attributes
    def test_attrs_type_validation(self):
        Base._Base__nb_objects = 0
        # Checking various invalid types for size
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("20", 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(4.3, 20)
        # Checking various invalid types for x and y
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(20, "x", 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(20, -42.3, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(20, 10, "y")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(20, 10, 5.2)
        # Checking other invalid types and values
        self.assertRaises(TypeError, Square, float("NaN"))
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, [10, 10], [10, 10], [10, 10])
        self.assertRaises(TypeError, Square, "abebe", "abebe", "abebe")
        self.assertRaises(TypeError, Square, 10, [10, 10], {10, 10})

    # Test case for checking value validation of attributes
    def test_attrs_value_validation(self):
        Base._Base__nb_objects = 0
        # Checking invalid values for size
        w_err = "width must be > 0"
        self.assertRaisesRegex(ValueError, w_err, Square, -20)
        self.assertRaisesRegex(ValueError, w_err, Square, 0)
        self.assertRaisesRegex(ValueError, w_err, Square, -20000000)
        # Checking invalid values for x and y
        x_err = "x must be >= 0"
        self.assertRaisesRegex(ValueError, x_err, Square, 10, -10)
        self.assertRaisesRegex(ValueError, x_err, Square, 10, -100000)
        y_err = "y must be >= 0"
        self.assertRaisesRegex(ValueError, y_err, Square, 10, 10, -10)
        self.assertRaisesRegex(ValueError, y_err, Square, 1, 1, -100000)

    # Test case for calculating area of Square
    def test_area(self):
        Base._Base__nb_objects = 0
        x = Square(10)
        self.assertEqual(x.area(), 100)
        x = Square(1234)
        self.assertEqual(x.area(), 1522756)
        x = Square(1)
        self.assertEqual(x.area(), 1)
        x = Square(43)
        self.assertEqual(x.area(), 1849)

    # Test case for displaying Square
    def test_display(self):
        Base._Base__nb_objects = 0
        captured_print = io.StringIO()
        sys.stdout = captured_print
        x = Square(2, 2, 2)
        x.display()
        self.assertEqual(captured_print.getvalue(), "\n\n  ##\n  ##\n")
        captured_print.seek(0)
        captured_print.truncate(0)
        x = Square(1, 1)
        x.display()
        self.assertEqual(captured_print.getvalue(), " #\n")
        captured_print.seek(0)
        captured_print.truncate(0)
        x = Square(1, 2, 2)
        x.display()
        self.assertEqual(captured_print.getvalue(), "\n\n  #\n")
        captured_print.seek(0)
        captured_print.truncate(0)
        sys.stdout = sys.__stdout__

    # Test case for string representation of Square
    def test_str(self):
        Base._Base__nb_objects = 0
        x = Square(1, 2, 2)
        self.assertEqual(x.__str__(), "[Square] (1) 2/2 - 1")
        x = Square(1, 1)
        self.assertEqual(x.__str__(), "[Square] (2) 1/0 - 1")
        x = Square(10000, 10000)
        self.assertEqual(x.__str__(), "[Square] (3) 10000/0 - 10000")

    # Test case for updating attributes of Square using args
    def test_args_update(self):
        Base._Base__nb_objects = 0
        x = Square(1, 2, 2)
        x.update(1, 10, 10, 20)
        self.assertEqual(x.__str__(), "[Square] (1) 10/20 - 10")
        x.update(1, 10, 10, 20, 20)
        self.assertEqual(x.__str__(), "[Square] (1) 10/20 - 10")
        x.update(1, 10, 10, 20, 20, 40, 50, 60)
        self.assertEqual(x.__str__(), "[Square] (1) 10/20 - 10")
        x.update(10)
        self.assertEqual(x.id, 10)
        x.update(13, 10, 20, 20)
        self.assertEqual(x.__str__(), "[Square] (13) 20/20 - 10")

    # Test case for updating attributes of Square using kwargs
    def test_kwargs_update(self):
        Base._Base__nb_objects = 0
        x = Square(1, 1, 2, 2)
        x.update(id=1, size=10, x=20, y=20)
        self.assertEqual(x.__str__(), "[Square] (1) 20/20 - 10")
        x.update(id=1, size=10, x=20, y=20, chala=40)
        self.assertEqual(x.__str__(), "[Square] (1) 20
