#!/usr/bin/env python3
"""Unit tests for utils module"""

from parameterized import parameterized
from typing import Any, Mapping, Sequence, Callable
import unittest
from unittest.mock import patch
import requests
from utils import memoize, get_json


class TestAcessNestedMap(unittest.TestCase):
    """Test case for util function `access_nested_map`
    """

    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": {"c": 3}}}, ("a", "b"), {"c": 3})
    ])
    def test_access_nested_map(
            self, nested_map: Mapping, keys: Sequence, result: Any) -> None:
        """Testing correct ouput is given"""
        output = None
        try:
            for key in keys:
                output = nested_map.get(key)
        except BaseException:
            pass
        self.assertEqual(output, result)

    @parameterized.expand([
        ({}, ("a", ), KeyError),
        ({"a": 1}, ("a", "b"), TypeError),
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, keys: Sequence,
            error: BaseException) -> None:
        """Testing incorrect output raises exception"""
        with self.assertRaises(error):
            for key in keys:
                nested_map[key]


class TestGetJson(unittest.TestCase):
    """Test case for util function `get_json`
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Any) -> None:
        """Testing correct output is given"""
        with patch("__main__.get_json") as mocked_function:
            def side_effect(test_url: str):
                """Side effect for mock function"""
                with patch("__main__.requests", "get") as mock:
                    mock.get(test_url)
                mock.assert_called_once_with(test_url)
            mocked_function.side_effect = side_effect
            mocked_function(test_url)
        mocked_function.assert_called_once_with(test_url)
        self.assertEqual(mocked_function.return_value, test_payload)


class TestMemoize(unittest.TestCase):
    """Test case for util function `memoize`
    """

    def test_memoize(self, fn: Callable) -> None:
        """Testing correct output is given"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_property", return_value=42
                          ) as mock_property:
            with patch.object(TestClass, "a_method", return_value=42
                              ) as mock_method:
                obj = TestClass()
                obj.a_property()
                obj.a_property()
        mock_property.assert_called()
        mock_method.assert_called_once()
        self.assertEqual(mock_property.return_value, 42)
        self.assertEqual(mock_method.return_value, 42)
