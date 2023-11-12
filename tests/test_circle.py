import unittest

from circle import *

class CircleTestCase(unittest.TestCase):
    '''
        Tests with null values for area
    '''
    def test_zero_area_1(self):
        result = area(0)
        self.assertEqual(result, 0)

    '''
        Tests with small values for area
    '''
    def test_small_area_1(self):
        result = area(19)
        self.assertEqual(result, 1134.1149479459152)

    def test_small_area_2(self):
        result = area(2)
        self.assertEqual(result, 12.566370614359172)

    def test_small_area_3(self):
        result = area(13)
        self.assertEqual(result, 530.929158456675)

    '''
        Tests with big values for area
    '''
    def test_big_area_1(self):
        result = area(19555842)
        self.assertEqual(result, 1201442282908392.2)

    def test_big_area_2(self):
        result = area(900007)
        self.assertEqual(result, 2544729633629.1055)

    def test_big_area_3(self):
        result = area(45888599)
        self.assertEqual(result, 6615451198920484.0)

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
        self.assertEqual(result, 87.96459430051421)

    def test_small_perimeter_2(self):
        result = perimeter(2)
        self.assertEqual(result, 12.566370614359172)

    def test_small_perimeter_3(self):
        result = perimeter(77)
        self.assertEqual(result, 483.80526865282815)

    '''
        Tests with big values for perimeter
    '''
    def test_big_perimeter_1(self):
        result = perimeter(19555842)
        self.assertEqual(result, 122872979.12392545)

    def test_big_perimeter_2(self):
        result = perimeter(888868888827)
        self.assertEqual(result, 5584927942286.852)

    def test_big_perimeter_3(self):
        result = perimeter(1090909092837263)
        self.assertEqual(result, 6854383983583702.0)
