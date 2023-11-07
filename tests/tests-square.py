import unittest

from lib.square import *

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_huge_area(self):
        result = area(9999999)
        expected_result = 99999980000001
        self.assertEqual(expected_result, result)

    def test_little_area(self):
        result = area(0.01)
        expected_result = 0.0001
        self.assertEqual(expected_result, result)

    def test_huge_perimeter(self):
        result = perimeter(9999999)
        expected_result = 39999996.0
        self.assertEqual(expected_result, result)

    def test_little_perimeter(self):
        result = perimeter(0.01)
        expected_result = 0.04
        self.assertEqual(expected_result, result)

    def test_zero_perimeter(self):
        result = perimeter(0)
        expected_result = 0
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
