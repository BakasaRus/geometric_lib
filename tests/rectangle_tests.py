import unittest, rectangle


class RectangleTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 0)

    def test_zero_sides_area(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_zero_sides_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_small_sides_area(self):
        res = rectangle.area(10, 5)
        self.assertEqual(res, 50)

    def test_small_sides_perimeter(self):
        res = rectangle.perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_big_sides_area(self):
        res = rectangle.area(1000000, 200000)
        self.assertEqual(res, 200000000000)

    def test_big_sides_perimeter(self):
        res = rectangle.perimeter(1000000, 200000)
        self.assertEqual(res, 2400000)

    def test_negative_side_area(self):
        self.assertRaises(ArithmeticError, rectangle.area, -3, 5)

    def test_negative_side_perimeter(self):
        self.assertRaises(ArithmeticError, rectangle.perimeter, -3, 5)
