import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_area_1(self):
        res = square.area(100)
        self.assertEqual(res, 100**2)

    def test_perimeter_2(self):
        res = square.perimeter(100)
        self.assertEqual(res, 400)


if __name__ == "__main__":
    unittest.main()
