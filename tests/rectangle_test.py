import unittest

import rectangle


class TestRectangleFunctions(unittest.TestCase):
    def test_area1(self):
        area = rectangle.area(2, 3)
        self.assertEqual(area, 6)

    def test_area2(self):
        area = rectangle.area(4, 5)
        self.assertEqual(area, 20)

    def test_zero_area(self):
        area = rectangle.area(0, 5)
        self.assertEqual(area, 0)

    def test_perimeter1(self):
        perimeter = rectangle.perimeter(2, 3)
        self.assertEqual(perimeter, 10)

    def test_perimeter2(self):
        perimeter = rectangle.perimeter(4, 5)
        self.assertEqual(perimeter, 18)

    def test_zero_perimeter(self):
        perimeter = rectangle.perimeter(0, 5)
        self.assertEqual(perimeter, 10)
