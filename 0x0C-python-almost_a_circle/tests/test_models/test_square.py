#!/usr/bin/python3
""" Unit tests for Square class """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test cases for Square class """

    def test_constructor(self):
        """ Test constructor """
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_str(self):
        """ Test string representation """
        s = Square(4, 1, 2, 7)
        self.assertEqual(str(s), "[Square] (7) 1/2 - 4")

    def test_size_getter_setter(self):
        """ Test size getter and setter """
        s = Square(3)
        self.assertEqual(s.size, 3)
        s.size = 6
        self.assertEqual(s.size, 6)

    def test_update(self):
        """ Test update method """
        s = Square(4, 1, 1, 1)
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")


if __name__ == '__main__':
    unittest.main()
