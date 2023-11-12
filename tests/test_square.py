import unittest

from square import *

class SquareTestCase(unittest.TestCase):
    '''
        Tests with small values for area
    '''
    def test_zero_area_1(self):
        result = area(0)
        self.assertEqual(result, 0)

    '''
        Tests with small values for area
    '''
    def test_small_area_1(self):
        result = area(19)
        self.assertEqual(result, 361)

    def test_small_area_2(self):
        result = area(2)
        self.assertEqual(result, 4)

    def test_small_area_3(self):
        result = area(13)
        self.assertEqual(result, 169)

    '''
        Tests with big values for area
    '''
    def test_big_area_1(self):
        result = area(19555842)
        self.assertEqual(result, 382430956328964)

    def test_big_area_2(self):
        result = area(900007000)
        self.assertEqual(result, 810012600049000000)

    def test_big_area_3(self):
        result = area(458885999)
        self.assertEqual(result, 210576360078228001)

    '''
        Tests with null values for perimeter
    '''
    def test_zero_perimeter_1(self):
        result = perimeter(0)
        self.assertEqual(result, 0)

    '''
        Tests with small values for perimeter
    '''
    def test_small_perimeter_1(self):
        result = perimeter(14)
        self.assertEqual(result, 56)

    def test_small_perimeter_2(self):
        result = perimeter(2)
        self.assertEqual(result, 8)

    def test_small_perimeter_3(self):
        result = perimeter(77)
        self.assertEqual(result, 308)

    '''
        Tests with big values for perimeter
    '''
    def test_big_perimeter_1(self):
        result = perimeter(19555842)
        self.assertEqual(result, 78223368)

    def test_big_perimeter_2(self):
        result = perimeter(888868888827)
        self.assertEqual(result, 3555475555308)

    def test_big_perimeter_3(self):
        result = perimeter(1090909092837263)
        self.assertEqual(result, 4363636371349052)
