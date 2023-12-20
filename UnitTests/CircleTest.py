import unittest, random
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertAlmostEqual(res, 0, delta=0.1)

    def test_numbers_area(self):
        res = area(6173390)
        self.assertAlmostEqual(res, 119728433662581.97, delta=0.1)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area('0')

    def test_float_area(self):
        res = area(913.8172)
        self.assertAlmostEqual(res, 2623424.251842681, delta=0.1)

    def test_zero_perim(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0, delta=0.1)

    def test_numbers_perim(self):
        res = perimeter(6173391)
        self.assertAlmostEqual(res, 38788559.63, delta=0.1)
    
    def test_string_perim(self):
        with self.assertRaises(TypeError):
            perimeter('0')
    
    def test_float_perim(self):
        res = perimeter(913.8172)
        self.assertAlmostEqual(res, 5741.682804487989, delta=0.1)