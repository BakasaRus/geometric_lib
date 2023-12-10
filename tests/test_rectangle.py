import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(0, 1)
        self.assertEqual(res, 0)

    def test_zero_arer_2(self):
        res = rectangle.area(1, 0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = rectangle.area(1, 1)
        self.assertEqual(res, 1)

    def test_two_square_area(self):
        res = rectangle.area(2, 2)
        self.assertEqual(res, 4)

    def test_half_area(self):
        res = rectangle.area(0.5, 0.5)
        self.assertAlmostEqual(res, 0.25, 0.000001)

    def test_third_area(self):
        res = rectangle.area(0.332, 3)
        self.assertAlmostEqual(res, 0.996, 0.000001)

    def test_big1_area(self):
        res = rectangle.area(12345, 2)
        self.assertEqual(res, 24690)

    def test_wrong_area(self):
        def test_wrong_area(self):
            with self.assertRaises(TypeError):
                rectangle.area("fef", "de")
    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)
        res = rectangle.perimeter(0, 1)
        self.assertEqual(res, 2)
        res = rectangle.perimeter(1, 0)
        self.assertEqual(res, 2)

    def test_one_perimeter(self):
        res = rectangle.perimeter(1, 1)
        self.assertEqual(res, 4)

    def test_two_perimeter(self):
        res = rectangle.perimeter(2, 1)
        self.assertEqual(res, 6)

    def test_half_perimeter(self):
        res = rectangle.perimeter(0.5, 0.5)
        self.assertAlmostEqual(res, 2, 0.000001)

    def test_third_perimeter(self):
        res = rectangle.perimeter(0.333, 1)
        self.assertAlmostEqual(res, 2.666, 0.000001)

    def test_big1_perimeter(self):
        res = rectangle.perimeter(12345, 1242)
        self.assertEqual(res, 27174)
