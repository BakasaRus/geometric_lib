import unittest

import square


class TestSquareFunctions(unittest.TestCase):
    def test_area1(self):
        area = square.area(2)
        self.assertEqual(area, 4)

    def test_area2(self):
        area = square.area(3)
        self.assertEqual(area, 9)

    def test_area3(self):
        area = square.area(7)
        self.assertEqual(area, 49)

    def test_zero_area(self):
        area = square.area(0)
        self.assertEqual(area, 0)

    def test_perimeter1(self):
        perimeter = square.perimeter(2)
        self.assertEqual(perimeter, 8)

    def test_perimeter2(self):
        perimeter = square.perimeter(3)
        self.assertEqual(perimeter, 12)

    def test_zero_perimeter(self):
        perimeter = square.perimeter(0)
        self.assertEqual(perimeter, 0)
