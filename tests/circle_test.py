import unittest
import math

import circle


class TestCircleFunctions(unittest.TestCase):
    def test_unit_area(self):
        area = circle.area(1)
        self.assertAlmostEqual(area, math.pi, places=2)

    def test_area1(self):
        area = circle.area(2)
        self.assertAlmostEqual(area, 4 * math.pi, places=2)

    def test_zero_area(self):
        area = circle.area(0)
        self.assertAlmostEqual(area, 0, places=2)

    def test_unit_perimeter(self):
        perimeter = circle.perimeter(1)
        self.assertAlmostEqual(perimeter, 2 * math.pi, places=2)

    def test_perimeter1(self):
        perimeter = circle.perimeter(2)
        self.assertAlmostEqual(perimeter, 4 * math.pi, places=2)

    def test_zero_perimeter(self):
        perimeter = circle.perimeter(0)
        self.assertAlmostEqual(perimeter, 0, places=2)
