import unittest
import circle


class TestCirce(unittest.TestCase):
    # Correct testing (positive numbers)
    def test_area_positive(self):
        res = circle.area(21642893)
        self.assertAlmostEqual(res, 1471568549206129.5)

        res = circle.area(2837498273498273947298)
        self.assertAlmostEqual(res, 2.5294207945074145e+43)

    def test_perimeter_positive(self):
        res = circle.perimeter(1)
        self.assertAlmostEqual(res, 6.283185307179586)

        res = circle.perimeter(18723)
        self.assertAlmostEqual(res, 117640.07850632339)

    def test_area_negative(self):
        res = circle.area(278364)
        self.assertNotAlmostEqual(res, 34628394792)

        res = circle.area(9876543)
        self.assertNotAlmostEqual(res, 89139.54995295679)

    def test_perimeter_negative(self):
        res = circle.perimeter(1e+100)
        self.assertNotAlmostEqual(res, 0)

        res = circle.perimeter(1)
        self.assertNotAlmostEqual(res, 3.1)

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

    # Speed testing
    def test_area_speed(self):
        res = circle.area(263846892348972983749823749872893749827349872398479283)
        self.assertAlmostEqual(res, 2.1870254624141658e+107)

        res = circle.area(90032220.84293322)
        self.assertAlmostEqual(res, 2.5465124213045796e+16)

    def test_perimeter_speed(self):
        res = circle.perimeter(256351728379203849023784528983942638428)
        self.assertAlmostEqual(res, 1.6107054132223058e+39)

        res = circle.perimeter(1.6107054132223058e+39)
        self.assertAlmostEqual(res, 1.0120360586553016e+40)
