import unittest

from lib.sphere import *
from resourses.algebra import *

class SphereTestCase(unittest.TestCase):
    def test_not_positive_input_area(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_huge_area(self):
        result = area(9999999)
        expected_result = 1256636810108517.5
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_little_area(self):
        result = area(0.1)
        expected_result = 0.12566370614359174
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_huge_volume(self):
        result = volume(9999999)
        expected_result = 4.188788948149455e+21
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_little_volume(self):
        result = volume(0.1)
        expected_result = 0.004188790204786391
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_not_positive_input_volume(self):
        with self.assertRaises(ValueError):
            volume(-1)


if __name__ == '__main__':
    unittest.main()
