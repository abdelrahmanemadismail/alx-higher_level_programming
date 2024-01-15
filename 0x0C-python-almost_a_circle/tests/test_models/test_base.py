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

    def test_to_json_string(self):
        """ Test to_json_string method """
        # Test with a non-empty list of dictionaries
        list_of_dicts = [{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 4, "y": 5}]
        json_string = Base.to_json_string(list_of_dicts)
        self.assertEqual(
                json_string,
                '[{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 4, "y": 5}]'
                )

        # Test with an empty list
        empty_list = []
        json_string_empty = Base.to_json_string(empty_list)
        self.assertEqual(json_string_empty, '[]')

        # Test with None
        json_string_none = Base.to_json_string(None)
        self.assertEqual(json_string_none, '[]')


if __name__ == '__main__':
    unittest.main()
