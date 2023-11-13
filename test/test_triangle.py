import unittest
import triangle


class TestTriangle(unittest.TestCase):
    # Correct testing (positive numbers)
    def test_area_positive(self):
        res = triangle.area(10, 15)
        self.assertEqual(res, 75)

        res = triangle.area(1, 50)
        self.assertEqual(res, 25)

    def test_perimeter_positive(self):
        res = triangle.perimeter(10, 25, 30)
        self.assertEqual(res, 65)

        res = triangle.perimeter(50, 80, 80)
        self.assertEqual(res, 210)

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
