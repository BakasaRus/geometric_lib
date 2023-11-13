import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle.area(0, 1)
        self.assertEqual(res, 0)
        res = triangle.area(1, 0)
        self.assertEqual(res, 0)
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = triangle.area(1, 1)
        self.assertAlmostEqual(res, 0.5, 0.000001)

    def test_two_square_area(self):
        res = triangle.area(1, 2)
        self.assertEqual(res, 1)

    def test_half_area(self):
        res = triangle.area(0.5, 8)
        self.assertEqual(res, 2)

    def test_small_area(self):
        res = triangle.area(0.02, 0.1)
        self.assertAlmostEqual(res, 0.001, 0.000001)

    def test_big1_area(self):
        res = triangle.area(12345, 241)
        self.assertEqual(res, 1487572.5)

    def test_big2_area(self):
        res = triangle.area(1020, 20)
        self.assertEqual(res, 10200)

    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = triangle.perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_two_perimeter(self):
        res = triangle.perimeter(2, 1, 2)
        self.assertEqual(res, 5)

    def test_half_perimeter(self):
        res = triangle.perimeter(0.5, 1, 1.5)
        self.assertAlmostEqual(res, 3, 0.000001)

    def test_third_perimeter(self):
        res = triangle.perimeter(0.333, 0.1, 0.2)
        self.assertAlmostEqual(res, 0.633, 0.000001)

    def test_big1_perimeter(self):
        res = triangle.perimeter(12345, 123, 7432)
        self.assertEqual(res, 19900)

    def test_big2_perimeter(self):
        res = triangle.perimeter(1020, 1, 10235)
        self.assertEqual(res, 11256)