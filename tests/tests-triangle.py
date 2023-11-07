import unittest

from lib.triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0, 0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_huge_area(self):
        result = area(9999999, 888888)
        expected_result = 4444439555556.0
        self.assertEqual(expected_result, result)

    def test_little_area(self):
        result = area(0.01, 0.1)
        expected_result = 0.0005
        self.assertEqual(expected_result, result)

    def test_huge_perimeter(self):
        result = perimeter(9999999, 8888888, 7777777)
        expected_result = 26666664
        self.assertEqual(expected_result, result)

    def test_little_perimeter(self):
        result = perimeter(0.01, 0.02, 0.03)
        expected_result = 0.06
        self.assertEqual(expected_result, result)

    def test_zero_perimeter(self):
        result = perimeter(0, 0, 0)
        expected_result = 0
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
