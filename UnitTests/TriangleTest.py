import unittest, random
from triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_numbers_area(self):
        res = area(6173391, 126381732)
        self.assertEqual(res, 390101923446606)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area('0', '91')

    def test_float_area(self):
        res = area(913.8172, 1273.671)
        self.assertAlmostEqual(res, 581951.2334706, delta=0.1)

    def test_zero_perim(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_numbers_perim(self):
        res = perimeter(6173391, 126371832, 981331)
        self.assertEqual(res, 133526554)
    
    def test_string_perim(self):
        with self.assertRaises(TypeError):
            perimeter('0', '10', '15')
    
    def test_float_perim(self):
        res = perimeter(913.8172, 1832.9123, 89123.6417)
        self.assertAlmostEqual(res, 91870.3712, delta=0.1)