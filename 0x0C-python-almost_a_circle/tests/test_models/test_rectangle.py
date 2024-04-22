#!/usr/bin/python3

import unittest
import io
import sys
# Importing Rectangle and Base classes from respective modules
from models.rectangle import Rectangle
from models.base import Base


class TestRectCls(unittest.TestCase):
    # Testing the initialization of Rectangle instances
    def test_init(self):
        Base._Base__nb_objects = 0
        x = Rectangle(10, 10)
        y = Rectangle(10, 10)
        self.assertEqual(x.id, 1)
        self.assertEqual(y.id, 2)

    # Testing attributes of Rectangle instances
    def test_attrs(self):
        Base._Base__nb_objects = 0
        x = Rectangle(10, 10, 10, 10, 15)
        self.assertEqual(x.width, 10)
        self.assertEqual(x.height, 10)
        self.assertEqual(x.x, 10)
        self.assertEqual(x.y, 10)
        self.assertEqual(x.id, 15)

    # Testing type validation of attributes
    def test_attrs_type_validation(self):
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("20", 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(20, "20")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(20, 20, "x", 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(20, 20, 10, "y")
        # Additional type validation tests
        self.assertRaises(TypeError, Rectangle, float("NaN"), float("inf"))
        # ...

    # Testing value validation of attributes
    def test_attrs_value_validation(self):
        Base._Base__nb_objects = 0
        w_err = "width must be > 0"
        self.assertRaisesRegex(ValueError, w_err, Rectangle, -20, 20)
        # ...

    # Testing the area calculation method
    def test_area(self):
        Base._Base__nb_objects = 0
        x = Rectangle(10, 10)
        self.assertEqual(x.area(), 100)
        # ...

    # Testing the display method
    def test_display(self):
        Base._Base__nb_objects = 0

        captured_print = io.StringIO()
        sys.stdout = captured_print

        x = Rectangle(2, 2, 2, 2)
        x.display()
        self.assertEqual(captured_print.getvalue(), "\n\n  ##\n  ##\n")
        # ...

    # Testing the string representation method
    def test_str(self):
        Base._Base__nb_objects = 0
        x = Rectangle(1, 1, 2, 2)
        self.assertEqual(x.__str__(), "[Rectangle] (1) 2/2 - 1/1")
        # ...

    # Testing update methods with different arguments and keyword arguments
    def test_args_update(self):
        # ...

    def test_kwargs_update(self):
        # ...

    def test_args_kwargs_update(self):
        # ...

    # Testing the to_dictionary method
    def test_to_dict(self):
        # ...


if __name__ == "__main__":
    unittest.main()
