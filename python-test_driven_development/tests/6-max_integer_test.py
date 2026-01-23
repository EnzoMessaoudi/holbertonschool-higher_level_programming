#!/usr/bin/python3


"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Function tests
    """
    def test_max_value(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertAlmostEqual(max_integer([-1, -6, -5, -8]), -1)

    def test_Errors(self):
        self.assertIsNone(max_integer([]))
