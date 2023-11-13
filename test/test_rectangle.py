import unittest
import rectangle


class TestRectangle(unittest.TestCase):
    # Correct testing (positive numbers)
    def test_area_positive(self):
        res = rectangle.area(10, 15)
        self.assertEqual(res, 150)

        res = rectangle.area(1, 50)
        self.assertEqual(res, 50)

    def test_perimeter_positive(self):
        res = rectangle.perimeter(10, 20)
        self.assertEqual(res, 60)

        res = rectangle.perimeter(50, 80)
        self.assertEqual(res, 260)

    # Failure (negative and strings)
    def test_area_failure(self):
        with self.assertRaises(ValueError):
            res = rectangle.area(-100, 10)

        with self.assertRaises(ValueError):
            res = rectangle.area(0, -1e+100000000)

        with self.assertRaises(ValueError):
            res = rectangle.area("23176548", 12)

        with self.assertRaises(ValueError):
            res = rectangle.area("3682", "12")

    def test_perimetr_failure(self):
        with self.assertRaises(ValueError):
            res = rectangle.perimeter(12, -10)

        with self.assertRaises(ValueError):
            res = rectangle.perimeter(-1, 1e+10000)

        with self.assertRaises(ValueError):
            res = rectangle.perimeter("32", 3)

        with self.assertRaises(ValueError):
            res = rectangle.perimeter("1234567890", "1234567890")
