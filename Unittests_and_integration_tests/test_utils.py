#!/usr/bin/env python3
"""Tests for utils.py
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{expected_key}'")


class TestGetJson(unittest.TestCase):

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            # Mock the response's json method
            mock_get.return_value.json.return_value = test_payload

            # Call the function
            result = get_json(test_url)

            # Assert the get method was called once with the correct URL
            mock_get.assert_called_once_with(test_url)

            # Assert the result is as expected
            self.assertEqual(result, test_payload)

            # Reset the mock to clear call history for the next iteration
            mock_get.reset_mock()

class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            obj = TestClass()

            # Call a_property twice
            result1 = obj.a_property
            result2 = obj.a_property

            # Verify the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Verify a_method was called only once
            mock_method.assert_called_once()
