import unittest
import circle


class TestCirce(unittest.TestCase):
    # Correct testing (positive numbers)
    def test_area_positive(self):
        res = circle.area(10)
        self.assertAlmostEqual(res, 314.159265359)

        res = circle.area(1.5)
        self.assertAlmostEqual(res, 7.068583471)

    def test_perimeter_positive(self):
        res = circle.perimeter(1)
        self.assertAlmostEqual(res, 6.283185307)

        res = circle.perimeter(158.852)
        self.assertAlmostEqual(res, 998.096552416)

    # Failure (negative, zero and strings)
    def test_area_failure(self):
        with self.assertRaises(ValueError):
            res = circle.area(-100)

        with self.assertRaises(ValueError):
            res = circle.area(0)

        with self.assertRaises(ValueError):
            res = circle.area("2389472")

    def test_perimeter_failure(self):
        with self.assertRaises(ValueError):
            res = circle.perimeter(0)

        with self.assertRaises(ValueError):
            res = circle.perimeter(-1)

        with self.assertRaises(ValueError):
            res = circle.area("08080")
