#!/usr/bin/python3
"""Unit test"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the max_integer fuction

    Args:
        unittest (unittest): _description_
    """
    def test_int_args(self):
        self.assertRaises(TypeError, max_integer, 2)

    def test_float_args(self):
        self.assertRaises(TypeError, max_integer, 2.0)

    def test_bool_arg(self):
        self.assertRaises(TypeError, max_integer, False)

    def test_string_in_list(self):
        self.assertRaises(TypeError, max_integer, [-5, 2, "100", -2])

    def test_none_list(self):
        self.assertRaises(TypeError, max_integer, [None, None])

    def test_nested_list(self):
        self.assertRaises(TypeError, max_integer, [2, [2, 3], 4])

    def test_tuple_in_list(self):
        self.assertRaises(TypeError, max_integer, [1, (2, 3)])

    def test_max_integer(self):
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)

    def test_only_negs(self):
        self.assertEqual(max_integer([-5, -2, -100, -3]), -2)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_list_comprehension(self):
        self.assertEqual(max_integer([i for i in range(5)]), 4)

    def test_repeated_numbers(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)
