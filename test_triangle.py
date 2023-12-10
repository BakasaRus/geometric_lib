import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_zero1(self):
        self.assertEqual(triangle.area(0, 5), -1)
        self.assertEqual(triangle.perimeter(0, 5, 0), -1)

    def test_zero2(self):
        self.assertEqual(triangle.area(5, 0), -1)
        self.assertEqual(triangle.perimeter(5, 0, 0), -1)

    def test_zero3(self):
        self.assertEqual(triangle.area(0, 0), -1)
        self.assertEqual(triangle.perimeter(0, 0, 0), -1)

    def test_one(self):
        self.assertEqual(triangle.area(1, 2), 1)
        self.assertEqual(triangle.perimeter(1, 2, 2.5), 5.5)

    def test_two(self):
        self.assertEqual(triangle.area(2, 4), 4)
        self.assertEqual(triangle.perimeter(2, 4, 5), 11)

    def test_five(self):
        self.assertEqual(triangle.area(5, 6), 15)
        self.assertEqual(triangle.perimeter(5, 6, 8), 19)

    def test_big_data(self):
        self.assertEqual(triangle.area(123_456_789, 1_234_567_890), 76_207_893_750_952_605)
        self.assertEqual(triangle.perimeter(123_456_789, 1_234_567_890, 1_234_567_890), 2_592_592_569)

    def test_float(self):
        self.assertEqual(triangle.area(0.5, 0.145), 0.03625)
        self.assertEqual(triangle.perimeter(0.5, 0.145, 0.147), 0.792)

    def test_negative1(self):
        self.assertEqual(triangle.area(-1, 1), -1)
        self.assertEqual(triangle.perimeter(-1, 1, 5), -1)

    def test_negative2(self):
        self.assertEqual(triangle.area(1, -1), -1)
        self.assertEqual(triangle.perimeter(1, -1, 5), -1)

    def test_negative3(self):
        self.assertEqual(triangle.area(-1, -1), -1)
        self.assertEqual(triangle.perimeter(-1, -1, -5), -1)

    def test_non_existent(self):
        self.assertEqual(triangle.perimeter(1, 5, 7), -1)
        self.assertEqual(triangle.perimeter(3, 4, 8), -1)
        self.assertEqual(triangle.perimeter(17, 7, 9), -1)
        self.assertEqual(triangle.perimeter(3, 28, 17), -1)
