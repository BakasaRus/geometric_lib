import square
import unittest

class SquarePerimeterTestCase(unittest.TestCase):
    def test_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_big(self):
        res = square.perimeter(408750)
        self.assertEqual(res, 1635000)
    
    def test_sample(self):
        res = square.perimeter(33)
        self.assertEqual(res, 132)

    def test_small(self):
        res = square.perimeter(1)
        self.assertEqual(res, 4)
    
    def test_negative(self):
        res = square.perimeter(-2)
        self.assertEqual(res, 0)

    def test_string(self):
        with self.assertRaises(TypeError):
            square.perimeter("Are str allowed?")
