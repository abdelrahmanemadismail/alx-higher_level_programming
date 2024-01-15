#!/usr/bin/python3
"""Unit tests for Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        b = Base(42)
        self.assertEqual(b.id, 42)

    def test_init_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)


if __name__ == '__main__':
    unittest.main()
