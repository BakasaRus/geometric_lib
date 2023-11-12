import unittest


def area(a, h):
    """Принимает длину стороны и высоты треугольника, возвращает площадь соответствующего треугольника"""
    return a * h / 2


def perimeter(a, b, c):
    """Принимает длины сторон треугольника, возвращает периметр соответствующего треугольника"""
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = area(0, 4)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = perimeter(0, 4, 6)
        self.assertEqual(res, 10)

    def test_zero_height_area(self):
        res = area(4, 0)
        self.assertEqual(res, 0)

    def test_zero_sides_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_positive_side_area(self):
        res = area(3, 4)
        self.assertEqual(res, 6)

    def test_positive_side_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_negative_side_area(self):
        res = area(-3, 4)
        self.assertEqual(res, -1)

    def test_negative_height_area(self):
        res = area(3, -4)
        self.assertEqual(res, -1)

    def test_negative_sides_perimeter(self):
        res = perimeter(-1, -2, 3)
        self.assertEqual(res, -1)
