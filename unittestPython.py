#!/usr/local/bin/python3

# Test file called test_math_operations.py
import unittest
from math_operations import add, subtract


class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test if 2 + 3 = 5
        self.assertEqual(add(-1, 1), 0)  # Test if -1 + 1 = 0

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)  # Test if 10 - 5 = 5
        self.assertEqual(subtract(0, 4), -4)  # Test if 0 - 4 = -4


if __name__ == "__main__":
    unittest.main()
