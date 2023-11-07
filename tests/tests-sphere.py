import unittest

from lib.sphere import *

class SphereTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_huge_area(self):
        result = area(9999999)
        expected_result = 1256636810108517.5
        self.assertEqual(expected_result, result)

    def test_little_area(self):
        result = area(0.1)
        expected_result = 0.12566370614359174
        self.assertEqual(expected_result, result)

    def test_huge_volume(self):
        result = volume(9999999)
        expected_result = 4.188788948149455e+21
        self.assertEqual(expected_result, result)

    def test_little_volume(self):
        result = volume(0.1)
        expected_result = 0.004188790204786391
        self.assertEqual(expected_result, result)

    def test_zero_volume(self):
        result = volume(0)
        expected_result = 0
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
