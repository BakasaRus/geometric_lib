import unittest

from lib.circle import *

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_huge_area(self):
        result = area(9999999)
        expected_result = 314159202527129.4
        self.assertEqual(expected_result, result)

    def test_little_area(self):
        result = area(0.1)
        expected_result = 0.031415926535897934
        self.assertEqual(expected_result, result)

    def test_huge_perimeter(self):
        result = perimeter(9999999)
        expected_result = 62831846.788610555
        self.assertEqual(expected_result, result)

    def test_little_perimeter(self):
        result = perimeter(0.1)
        expected_result = 0.6283185307179586
        self.assertEqual(expected_result, result)

    def test_zero_perimeter(self):
        result = perimeter(0)
        expected_result = 0
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
