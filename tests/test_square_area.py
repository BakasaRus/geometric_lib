import square
import unittest


class SquareAreaTestCase(unittest.TestCase):
    def test_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_big(self):
        res = square.area(408750)
        self.assertEqual(res, 167076562500)
    
    def test_sample(self):
        res = square.area(33)
        self.assertEqual(res, 1089)

    def test_small(self):
        res = square.area(1)
        self.assertEqual(res, 1)
    
    def test_negative(self):
        with self.assertRaises(ValueError):
            square.area(-2)

    def test_string(self):
        with self.assertRaises(TypeError):
            square.area("Are str allowed?")