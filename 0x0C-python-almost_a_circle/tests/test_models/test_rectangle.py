#!/usr/bin/python3
""" Unit tests for Rectangle class """
import unittest
import io
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for Rectangle class """

    def test_constructor(self):
        """ Test constructor method """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_width_validation(self):
        """ Test width validation """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)
        with self.assertRaises(TypeError):
            r = Rectangle("string", 2)

    def test_height_validation(self):
        """ Test height validation """
        with self.assertRaises(ValueError):
            r = Rectangle(2, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(2, -1)
        with self.assertRaises(TypeError):
            r = Rectangle(2, "string")

    def test_x_validation(self):
        """ Test x validation """
        with self.assertRaises(ValueError):
            r = Rectangle(2, 3, -1)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, "string")

    def test_y_validation(self):
        """ Test y validation """
        with self.assertRaises(ValueError):
            r = Rectangle(2, 3, 4, -1)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 4, "string")

    def test_area(self):
        """ Test area method """
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        """ Test display method """
        r = Rectangle(2, 3)
        with patch('sys.stdout', new_callable=io.StringIO) as ms:
            r.display()
            self.assertEqual(ms.getvalue(), "##\n##\n##\n")

    def test_str(self):
        """ Test __str__ method """
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_with_offset(self):
        """ Test display method with x and y offset """
        r = Rectangle(2, 3, 2, 2)
        with patch('sys.stdout', new_callable=io.StringIO) as ms:
            r.display()
            self.assertEqual(ms.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_update(self):
        """ Test update method """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")

        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_with_kwargs(self):
        """ Test update method with keyword arguments """
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=89, width=5, height=4, x=7, y=1)
        self.assertEqual(str(r), "[Rectangle] (89) 7/1 - 5/4")

    def test_update_with_args_and_kwargs(self):
        """ Test update method with both positional and keyword arguments """
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(89, 2, 3, 4, 5, id=90, width=3, height=4, x=6, y=7)
        self.assertEqual(str(r), "[Rectangle] (90) 6/7 - 3/4")

    def test_to_dictionary(self):
        """ Test to_dictionary method """
        r = Rectangle(4, 3, 2, 1, 5)
        dictionary = r.to_dictionary()
        expected_dict = {'id': 5, 'width': 4, 'height': 3, 'x': 2, 'y': 1}
        self.assertEqual(dictionary, expected_dict)


if __name__ == '__main__':
    unittest.main()
