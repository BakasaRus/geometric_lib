import circle
import unittest, math


class CircleAreaTestCase(unittest.TestCase):
    def test_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_big(self):
        res = circle.area(408750)
        self.assertEqual(res, math.pi * 167076562500)

    def test_sample(self):
        res = circle.area(36)
        self.assertEqual(res, math.pi * 1296)

    def test_small(self):
        res = circle.area(1)
        self.assertEqual(res, math.pi)
    
    def test_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-1)

    def test_string(self):
        with self.assertRaises(TypeError):
            circle.area("Are strings allowed?")

