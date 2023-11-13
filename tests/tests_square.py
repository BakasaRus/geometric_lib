import unittest

from lib.square import *
from resourses.algebra import *

class SquareTestCase(unittest.TestCase):
    def test_not_positive_input_area(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_huge_area(self):
        result = area(9999999)
        expected_result = 99999980000001
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_little_area(self):
        result = area(0.01)
        expected_result = 0.0001
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_huge_perimeter(self):
        result = perimeter(9999999)
        expected_result = 39999996.0
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_little_perimeter(self):
        result = perimeter(0.01)
        expected_result = 0.04
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_not_positive_input_perimetr(self):
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == '__main__':
    unittest.main()
