import math
import unittest
import circle, rectangle, square, triangle


class CircleAreaTestCase(unittest.TestCase):
    def test_circle_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_circle_simple_area(self):
        res = circle.area(3)
        self.assertEqual(res, 9 * math.pi)

    def test_circle_difficult_area(self):
        res = circle.area(100)
        self.assertEqual(res, 10000 * math.pi)

    def test_circle_neg_area(self):
        res = circle.area(-1)
        self.assertEqual(res, 0)


class RectangleAreaTestCase(unittest.TestCase):
    def test_rectangle_zero_area(self):
        res = rectangle.area(3, 0)
        self.assertEqual(res, 0)

    def test_rectangle_simple_area(self):
        res = rectangle.area(3, 7)
        self.assertEqual(res, 21)

    def test_rectangle_difficult_area(self):
        res = rectangle.area(100, 250)
        self.assertEqual(res, 100 * 250)

    def test_rectangle_neg_area(self):
        res = rectangle.area(-1, 250)
        self.assertEqual(res, 0)


class SquareAreaTestCase(unittest.TestCase):
    def test_square_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_square_simple_area(self):
        res = square.area(3)
        self.assertEqual(res, 9)

    def test_square_difficult_area(self):
        res = square.area(100)
        self.assertEqual(res, 10000)

    def test_square_neg_area(self):
        res = square.area(-1)
        self.assertEqual(res, 0)


class TriangleAreaTestCase(unittest.TestCase):
    def test_triangle_zero_area(self):
        res = triangle.area(3, 0)
        self.assertEqual(res, 0)

    def test_triangle_simple_area(self):
        res = triangle.area(3, 7)
        self.assertEqual(res, 21 / 2)

    def test_triangle_difficult_area(self):
        res = triangle.area(100, 250)
        self.assertEqual(res, 100 * 250 / 2)

    def test_triangle_neg_area(self):
        res = triangle.area(-3, -7)
        self.assertEqual(res, 0)


class CirclePerimeterTestCase(unittest.TestCase):
    def test_circle_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_simple_perimeter(self):
        res = circle.perimeter(3)
        self.assertEqual(res, 2 * 3 * math.pi)

    def test_circle_difficult_perimeter(self):
        res = circle.perimeter(100)
        self.assertEqual(res, 2 * 100 * math.pi)

    def test_circle_neg_perimeter(self):
        res = circle.perimeter(-1)
        self.assertEqual(res, 0)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_rectangle_zero_perimeter(self):
        res = rectangle.perimeter(3, 0)
        self.assertEqual(res, 0)

    def test_rectangle_simple_perimeter(self):
        res = rectangle.perimeter(3, 7)
        self.assertEqual(res, 2 * (3 + 7))

    def test_rectangle_difficult_perimeter(self):
        res = rectangle.perimeter(100, 250)
        self.assertEqual(res, 2 * 100 + 2 * 250)

    def test_rectangle_neg_perimeter(self):
        res = rectangle.perimeter(-3, -7)
        self.assertEqual(res, 0)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_square_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_square_simple_perimeter(self):
        res = square.perimeter(3)
        self.assertEqual(res, 12)

    def test_square_difficult_perimeter(self):
        res = square.perimeter(100)
        self.assertEqual(res, 400)

    def test_square_neg_perimeter(self):
        res = square.perimeter(-1)
        self.assertEqual(res, 0)


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_triangle_zero_perimeter(self):
        res = triangle.perimeter(3, 7, 0)
        self.assertEqual(res, 0)

    def test_triangle_simple_area(self):
        res = triangle.perimeter(3, 7, 9)
        self.assertEqual(res, 19)

    def test_triangle_difficult_area(self):
        res = triangle.perimeter(100, 250, 150)
        self.assertEqual(res, 500)

    def test_triangle_neg_area(self):
        res = triangle.perimeter(-1, 7, 9)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unit_test()