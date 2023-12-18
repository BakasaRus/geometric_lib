import unittest
import square


class TestSquare(unittest.TestCase):
    # Correct testing (positive numbers)
    def test_area_positive(self):
        res = square.area(10)
        self.assertEqual(res, 100)

        res = square.area(45.4851)
        self.assertEqual(res, 2068.8943220100005)

    def test_perimeter_positive(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

        res = square.perimeter(50)
        self.assertEqual(res, 200)

    # Failure (negative, zero and strings)
    def test_area_failure(self):
        with self.assertRaises(ValueError):
            res = square.area(-10008)

        with self.assertRaises(ValueError):
            res = square.area(0)

        with self.assertRaises(ValueError):
            res = square.area("1e+13849000")

    def test_perimeter_failure(self):
        with self.assertRaises(ValueError):
            res = square.perimeter(-14567)

        with self.assertRaises(ValueError):
            res = square.perimeter(0)

        with self.assertRaises(ValueError):
            res = square.area("287364")

