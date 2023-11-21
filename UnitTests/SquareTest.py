import unittest, random
from square import *

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_numbers_area(self):
        res = area(6173391)
        self.assertEqual(res, 38110756438881)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area('0')

    def test_float_area(self):
        res = area(913.8172)
        self.assertAlmostEqual(res, 835061.8750158399, delta=0.1)

    def test_zero_perim(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_numbers_perim(self):
        res = perimeter(6173391)
        self.assertEqual(res, 24693564)
    
    def test_string_perim(self):
        with self.assertRaises(TypeError):
            perimeter('0')
    
    def test_float_perim(self):
        res = perimeter(913.8172)
        self.assertAlmostEqual(res, 3655.2688, delta=0.1)