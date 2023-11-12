import unittest

from triangle import *

class TriangleTestCase(unittest.TestCase):
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
        self.assertEqual(result, 133)

    def test_small_area_2(self):
        result = area(2, 8)
        self.assertEqual(result, 8)

    def test_small_area_3(self):
        result = area(12.8, 10)
        self.assertEqual(result, 64)

    '''
        Tests with big values for area
    '''
    def test_big_area_1(self):
        result = area(19555842, 98888453)
        self.assertEqual(result, 966923481246213)

    def test_big_area_2(self):
        result = area(900007000, 4660008)
        self.assertEqual(result, 2097019910028000)

    def test_big_area_3(self):
        result = area(458885999.2, 78880000040.4)
        self.assertEqual(result, 18098463817717496183.84)

    '''
        Tests with null values for perimeter
    '''
    def test_zero_perimeter_1(self):
        result = perimeter(0, 14, 1)
        self.assertEqual(result, 15)

    def test_zero_perimeter_2(self):
        result = perimeter(2, 0, 0)
        self.assertEqual(result, 2)

    def test_zero_area_3(self):
        result = perimeter(0, 0, 0)
        self.assertEqual(result, 0)

    '''
        Tests with small values for perimeter
    '''
    def test_small_perimeter_1(self):
        result = perimeter(19, 14, 22)
        self.assertEqual(result, 55)

    def test_small_perimeter_2(self):
        result = perimeter(2, 8, 7)
        self.assertEqual(result, 17)

    def test_small_perimeter_3(self):
        result = perimeter(12.8, 10, 17.5)
        self.assertEqual(result, 40.3)

    '''
        Tests with big values for perimeter
    '''
    def test_big_perimeter_1(self):
        result = perimeter(19555842, 98888453, 96332)
        self.assertEqual(result, 118540627)

    def test_big_perimeter_2(self):
        result = perimeter(900007000, 4660008, 888868888827)
        self.assertEqual(result, 889773555835)

    def test_big_perimeter_3(self):
        result = perimeter(458885999, 78880000040, 9989836653)
        self.assertEqual(result, 89328722692)
