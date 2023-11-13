import unittest
import triangle


class TestTriangle(unittest.TestCase):
    # Correct testing (positive numbers)
    def test_area_positive(self):
        res = triangle.area(20, 25)
        self.assertEqual(res, 250)

        res = triangle.area(1, 500)
        self.assertEqual(res, 250)

    def test_perimeter_positive(self):
        res = triangle.perimeter(10, 20, 20)
        self.assertEqual(res, 50)

        res = triangle.perimeter(80, 80, 80)
        self.assertEqual(res, 240)

    def test_area_negative(self):
        res = triangle.area(10, 100)
        self.assertNotEqual(res, 5000)

        res = triangle.area(250, 50)
        self.assertNotEqual(res, 62500)

    def test_perimeter_negative(self):
        res = triangle.perimeter(100, 100, 50)
        self.assertNotEqual(res, 350)

        res = triangle.perimeter(1, 1, 1)
        self.assertNotEqual(res, 3.0000000000011)

    # Failure (negative, zero and strings)
    def test_area_failure(self):
        with self.assertRaises(ValueError):
            res = triangle.area(-100, "10")

        with self.assertRaises(ValueError):
            res = triangle.area(0, 1e+100000000)

    def test_perimeter_failure(self):
        with self.assertRaises(ValueError):
            res = triangle.perimeter("-1", 0, 50)

        with self.assertRaises(ValueError):
            res = triangle.perimeter(150, 50, 100)

    # Speed testing
    def test_area_speed(self):
        res = triangle.area(
            99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,
            99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
        self.assertAlmostEqual(res, 5e+207)

    def test_perimeter_speed(self):
        res = triangle.perimeter(2222222222222222222222222222222222222222222222222222222222222222222,
                                 2222222222222222222222222222222222222222222222222222222222222222222,
                                 2222222222222222222222222222222222222222222222222222222222222222222)
        self.assertEqual(res, 6666666666666666666666666666666666666666666666666666666666666666666)
