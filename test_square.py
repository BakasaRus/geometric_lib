import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(square.area(0), -1)
        self.assertEqual(square.perimeter(0), -1)

    def test_one(self):
        self.assertEqual(square.area(1), 1)
        self.assertEqual(square.perimeter(1), 4)

    def test_two(self):
        self.assertEqual(square.area(2), 4)
        self.assertEqual(square.perimeter(2), 8)

    def test_five(self):
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.perimeter(5), 20)

    def test_big_data(self):
        self.assertEqual(square.area(123_456_789), 15_241_578_750_190_521)
        self.assertEqual(square.perimeter(123_456_789), 493_827_156)

    def test_float(self):
        self.assertEqual(square.area(0.5), 0.25)
        self.assertEqual(square.perimeter(0.5), 2)

    def test_negative(self):
        self.assertEqual(square.area(-1), -1)
        self.assertEqual(square.perimeter(-1), -1)
