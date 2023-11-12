import math
import unittest
import circle
import rectangle
import square
import triangle

class RectangleTest(unittest.TestCase):
    def test_null_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_not_null_perimeter(self):
        res = rectangle.perimeter(23, 7)
        self.assertEqual(res, 60)

    def test_null_area(self):
        res = rectangle.area(12, 0)
        self.assertEqual(res, 0)

    def test_not_null_area(self):
        res = rectangle.area(12, 5)
        self.assertEqual(res, 60)

class TriangleTest(unittest.TestCase):
    def test_null_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_not_null_perimeter(self):
        res = triangle.perimeter(23, 7, 10)
        self.assertEqual(res, 40)

    def test_null_area(self):
        res = triangle.area(12, 0)
        self.assertEqual(res, 0)

    def test_not_null_area(self):
        res = triangle.area(12, 5)
        self.assertEqual(res, 30)

class CircleTest(unittest.TestCase):
    def test_null_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_not_null_perimeter(self):
        res = circle.perimeter(23)
        self.assertEqual(res, 2 * math.pi * 23)

    def test_null_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_not_null_area(self):
        res = circle.area(12)
        self.assertEqual(res, math.pi * 144)

class SquareTest(unittest.TestCase):
    def test_null_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_not_null_perimeter(self):
        res = square.perimeter(23)
        self.assertEqual(res, 92)

    def test_null_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_not_null_area(self):
        res = square.area(12)
        self.assertEqual(res, 144)
