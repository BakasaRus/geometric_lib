import unittest
import rectangle


class TestRectangle(unittest.TestCase):
    # Correct testing (positive numbers)
    def test_area_positive(self):
        res = rectangle.area(12, 15)
        self.assertEqual(res, 180)

        res = rectangle.area(2, 30)
        self.assertEqual(res, 60)

    def test_perimeter_positive(self):
        res = rectangle.perimeter(15, 20)
        self.assertEqual(res, 70)

        res = rectangle.perimeter(50, 85)
        self.assertEqual(res, 270)

    def test_area_negative(self):
        res = rectangle.area(15, 15)
        self.assertNotEqual(res, 50)

        res = rectangle.area(25, 50)
        self.assertNotEqual(res, 6000)

    def test_perimeter_negative(self):
        res = rectangle.perimeter(100, 10)
        self.assertNotEqual(res, 110)

        res = rectangle.perimeter(1, 1)
        self.assertNotEqual(res, 1)

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

    # Speed testing (big values)
    def test_area_speed(self):
        res = rectangle.area(12345678901234567890, 12345678901234567890)
        self.assertEqual(res, 152415787532388367501905199875019052100)

    def test_perimeter_speed(self):
        res = rectangle.perimeter(999999999999999999999999999999999, 999999999999999999999999999999999)
        self.assertEqual(res, 3999999999999999999999999999999996)
