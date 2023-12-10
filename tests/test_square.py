import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = square.area(1)
        self.assertEqual(res, 1)

    def test_two_square_area(self):
        res = square.area(2)
        self.assertEqual(res, 4)

    def test_half_area(self):
        res = square.area(0.5)
        self.assertAlmostEqual(res, 0.25, 0.000001)

    def test_small_area(self):
        res = square.area(0.02)
        self.assertAlmostEqual(res, 0.0004, 0.000001)

    def test_big1_area(self):
        res = square.area(12345)
        self.assertEqual(res, 152399025)

    def test_big2_area(self):
        res = square.area(1020)
        self.assertEqual(res, 1040400)

    def test_wrong_area(self):
        def test_wrong_area(self):
            with self.assertRaises(Exception):
                square.area("fef")
    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = square.perimeter(1)
        self.assertEqual(res, 4)

    def test_two_perimeter(self):
        res = square.perimeter(2)
        self.assertEqual(res, 8)

    def test_half_perimeter(self):
        res = square.perimeter(0.5)
        self.assertEqual(res, 2)

    def test_third_perimeter(self):
        res = square.perimeter(0.333)
        self.assertAlmostEqual(res, 1.332, 0.000001)

    def test_big1_perimeter(self):
        res = square.perimeter(12345)
        self.assertEqual(res, 49380)

    def test_big2_perimeter(self):
        res = square.perimeter(1020)
        self.assertEqual(res, 4080)

    def test_wrong_perimeter(self):
        with self.assertRaises(TypeError):
            square.perimeter("feffew1")