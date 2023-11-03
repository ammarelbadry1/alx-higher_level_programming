#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Represent max_integer test suite."""

    def test_empty(self):
        """Test empty list."""
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([1]), 1)

    def test_max_at_end(self):
        """Test a list with max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_middle(self):
        """Test a list with max at the middle."""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list with max at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_negative(self):
        """Test a list with a negative integer."""
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)

    def test_all_negative(self):
        """Test a list with all negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_two_max(self):
        """Test a list with repeated elements."""
        self.assertEqual(max_integer([1, 2, 2, 3, 4, 4]), 4)

    def test_all_integers(self):
        """Test a list with different elements and same types."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_integers_floats(self):
        """Test a list with integers and floats."""
        self.assertEqual(max_integer([1, 2, 3.3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4.2]), 4.2)

    def test_wrong_type(self):
        """Test a list with different elements and different types."""
        with self.assertRaises(TypeError):
            max_integer([1, "s", 2.3])
        with self.assertRaises(TypeError):
            max_integer([1, [1], 2.3])

    def test_wrong_input(self):
        """Test wrong input to the function."""
        with self.assertRaises(TypeError):
            max_integer(1)
        with self.assertRaises(KeyError):
            max_integer({1: 1})

    def test_different_valid_input(self):
        """Test string and tuple input to the function."""
        self.assertEqual(max_integer("123abc"), "c")
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)
