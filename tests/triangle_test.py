import unittest

import triangle


class TestTriangleFunctions(unittest.TestCase):
    def test_area1(self):
        area = triangle.area(2, 3)
        self.assertEqual(area, 3)

    def test_area2(self):
        area = triangle.area(4, 5)
        self.assertEqual(area, 10)

    def test_zero_area(self):
        area = triangle.area(0, 5)
        self.assertEqual(area, 0)

    def test_perimeter1(self):
        perimeter = triangle.perimeter(2, 3, 4)
        self.assertEqual(perimeter, 9)

    def test_perimeter2(self):
        perimeter = triangle.perimeter(4, 5, 6)
        self.assertEqual(perimeter, 15)

    def test_zero_perimeter(self):
        perimeter = triangle.perimeter(0, 5, 6)
        self.assertEqual(perimeter, 11)
