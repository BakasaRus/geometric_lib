import random, unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_numbers_area(self):
        res = area(6173391, 1572631732)
        self.assertEqual(res, 9708470580643212)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area('0', '10')

    def test_float_area(self):
        res = area(913.8172, 1723.71238)
        self.assertAlmostEqual(res, 1575158.020696936, delta=0.1)
    
    def test_zero_perim(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_same_numbers_perim(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_numbers_perim(self):
        res = perimeter(6173391, 1572631732)
        self.assertEqual(res, 3157610246)

    def test_string_perim(self):
        with self.assertRaises(TypeError):
            area('0', '10')

    def test_float_perim(self):
        res = perimeter(913.8172, 1723.71238)
        self.assertAlmostEqual(res, 5275.05916, delta=0.1)