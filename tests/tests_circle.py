import unittest

from lib.circle import *
from resourses.algebra import *

class CircleTestCase(unittest.TestCase):
    def test_not_positive_input_area(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_huge_area(self):
        result = area(9999999)
        expected_result = 314159202527129.4
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_little_area(self):
        result = area(0.1)
        expected_result = 0.031415926535897934
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_huge_perimeter(self):
        result = perimeter(9999999)
        expected_result = 62831846.788610555
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_little_perimeter(self):
        result = perimeter(0.1)
        expected_result = 0.6283185307179586
        inaccuracy = get_inaccuracy(result, expected_result)
        eps = 1e-6
        self.assertGreaterEqual(eps, inaccuracy)

    def test_not_positive_input_perimetr(self):
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == '__main__':
    unittest.main()
