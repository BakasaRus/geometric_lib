import unittest

from lib.triangle import *
from resourses.algebra import *

class TriangleTestCase(unittest.TestCase):
    def test_not_positive_input_area(self):
        with self.assertRaises(ValueError):
            area(-1, 0)

    def test_huge_area(self):
        result = area(9999999, 888888)
        expected_result = 4444439555556.0
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_little_area(self):
        result = area(0.01, 0.1)
        expected_result = 0.0005
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_huge_perimeter(self):
        result = perimeter(9999999, 8888888, 7777777)
        expected_result = 26666664
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_little_perimeter(self):
        result = perimeter(0.02, 0.02, 0.03)
        expected_result = 0.07
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_not_positive_input_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-1, 0, -1)

    def test_degenerate_triangle_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10)


if __name__ == '__main__':
    unittest.main()
