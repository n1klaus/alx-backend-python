#!/usr/bin/env python3
"""Unit tests for utils module"""

from parameterized import parameterized
from typing import Any, Mapping, Sequence
import unittest
from unittest.mock import patch, Mock
import requests
from utils import memoize, get_json


class TestAccessNestedMap(unittest.TestCase):
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
        try:
            for key in keys:
                nested_map = nested_map[key]
        except BaseException:
            pass
        self.assertEqual(nested_map, result)

    @parameterized.expand([
        ({}, ("a", ), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
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
        def side_effect(test_url: str):
            """Side effect for mock function"""
            with patch.object(requests, "get", autospec=True) as mock:
                my_payload = Mock(spec=object)
                setattr(my_payload, "json", lambda: test_payload)
                mock.return_value = my_payload
                result = get_json(test_url)
                self.assertEqual(result, test_payload)
            mock.assert_called_once_with(test_url)
            return test_payload

        mocked_function = Mock(get_json)
        mocked_function.side_effect = side_effect
        result = mocked_function(test_url)
        mocked_function.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test case for util function `memoize`
    """

    def test_memoize(self) -> None:
        """Testing correct output is given"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=lambda: 42
                          ) as mock_method:
            obj = TestClass()
            self.assertEqual(obj.a_property(), 42)
            self.assertEqual(obj.a_property(), 42)
            mock_method.assert_called_once()
