import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_zero_height_area(self):
        res = triangle.area(0, 2)
        self.assertEqual(res, 0)

    def test_zero_side_area(self):
        res = triangle.area(2, 0)
        self.assertEqual(res, 0)

    def test_area_1(self):
        res = triangle.area(1, 1)
        self.assertEqual(res, 0.5)

    def test_perimeter_1(self):
        res = triangle.perimeter(100, 100, 100)
        self.assertEqual(res, 300)


if __name__ == "__main__":
    unittest.main()
