import unittest, triangle


class TriangleTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = triangle.area(0, 4)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = triangle.perimeter(0, 4, 6)
        self.assertEqual(res, 10)

    def test_zero_height_area(self):
        res = triangle.area(4, 0)
        self.assertEqual(res, 0)

    def test_zero_sides_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_positive_side_area(self):
        res = triangle.area(3, 4)
        self.assertEqual(res, 6)

    def test_positive_side_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_negative_side_area(self):
        self.assertRaises(ArithmeticError, triangle.area, -3, 4)

    def test_negative_height_area(self):
        self.assertRaises(ArithmeticError, triangle.area, 3, -4)

    def test_negative_sides_perimeter(self):
        self.assertRaises(ArithmeticError, triangle.perimeter, -1, 2, 3)

    def test_not_existing_triangle_perimeter(self):
        self.assertRaises(ArithmeticError, triangle.perimeter, 1, 3, 4)
