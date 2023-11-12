import unittest

from rectangle import *

class RectangleTestCase(unittest.TestCase):
    '''
        Tests with null values for area
    '''
    def test_zero_area_1(self):
        result = area(0, 14)
        self.assertEqual(result, 0)

    def test_zero_area_2(self):
        result = area(2, 0)
        self.assertEqual(result, 0)

    def test_zero_area_3(self):
        result = area(0, 0)
        self.assertEqual(result, 0)

    '''
        Tests with small values for area
    '''
    def test_small_area_1(self):
        result = area(19, 14)
        self.assertEqual(result, 266)

    def test_small_area_2(self):
        result = area(2, 8)
        self.assertEqual(result, 16)

    def test_small_area_3(self):
        result = area(12.8, 10)
        self.assertEqual(result, 128)

    '''
        Tests with big values for area
    '''
    def test_big_area_1(self):
        result = area(19555842, 98888453)
        self.assertEqual(result, 1933846962492426)

    def test_big_area_2(self):
        result = area(900007000, 4660008)
        self.assertEqual(result, 4194039820056000)

    def test_big_area_3(self):
        result = area(458885999, 78880000040)
        self.assertEqual(result, 36196927619475439960)

    '''
        Tests with null values for perimeter
    '''
    def test_zero_perimeter_1(self):
        result = perimeter(0, 14)
        self.assertEqual(result, 28)

    def test_zero_perimeter_2(self):
        result = perimeter(2, 0)
        self.assertEqual(result, 4)

    def test_zero_area_3(self):
        result = perimeter(0, 0)
        self.assertEqual(result, 0)

    '''
        Tests with small values for perimeter
    '''
    def test_small_perimeter_1(self):
        result = perimeter(19, 14)
        self.assertEqual(result, 66)

    def test_small_perimeter_2(self):
        result = perimeter(2, 8)
        self.assertEqual(result, 20)

    def test_small_perimeter_3(self):
        result = perimeter(12, 10)
        self.assertEqual(result, 44)

    '''
        Tests with big values for perimeter
    '''
    def test_big_perimeter_1(self):
        result = perimeter(19555842, 98888453)
        self.assertEqual(result, 236888590)

    def test_big_perimeter_2(self):
        result = perimeter(4660008, 888868888827)
        self.assertEqual(result, 1777747097670)

    def test_big_perimeter_3(self):
        result = perimeter(78880000040, 9989836653)
        self.assertEqual(result, 177739673386)
