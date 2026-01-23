#!/usr/bin/python3


"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_result(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -6, -5, -8]), -1)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-10, 5, 3, -2, 0]), 5)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)
        self.assertEqual(max_integer([1000000, 999999, 13455001]), 13455001)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_Errors(self):
        self.assertIsNone(max_integer([]))
