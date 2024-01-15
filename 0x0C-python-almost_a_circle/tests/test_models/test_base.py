#!/usr/bin/python3
"""Unit tests for Base class"""

import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle


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

    def test_save_to_file(self):
        """ Test save_to_file method """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            file_contents = file.read()
            expected_content = json.loads(
                '[{"y": 8, "x": 2, "id": 3, "width": 10, "height": 7}, ' +
                '{"y": 0, "x": 0, "id": 4, "width": 2, "height": 4}]'
            )
            actual_content = json.loads(file_contents)
            self.assertEqual(expected_content, actual_content)

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string"""
        json_string = "[]"
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_non_empty(self):
        """Test from_json_string with a non-empty string"""
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        expect_result = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expect_result)

    def test_from_json_string_none(self):
        """Test from_json_string with None"""
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_invalid_json(self):
        """Test from_json_string with an invalid JSON string"""
        json_string = "invalid_json"
        with self.assertRaises(ValueError):
            Base.from_json_string(json_string)


if __name__ == '__main__':
    unittest.main()
