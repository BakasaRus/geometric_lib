import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(0, 1)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = rectangle.area(1, 0)
        self.assertEqual(res, 0)

    def test_square(self):
        res = rectangle.area(2, 2)
        self.assertEqual(res, 4)


if __name__ == "__main__":
    unittest.main()
