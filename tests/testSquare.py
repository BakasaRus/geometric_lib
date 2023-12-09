import square
import unittest


class SquareTestCaseArea(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertRaises(ValueError, square.area, -1)

    def testSimpleSides(self):
        self.assertEqual(square.area(3), 9)

    def testZeroSides(self):
        self.assertEqual(square.area(0), 0)

    def testBigSides(self):
        self.assertEqual(square.area(10_000), 100_000_000)


class SquareTestCasePerimeter(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertRaises(ValueError, square.perimeter, -1)

    def testSimpleSides(self):
        self.assertEqual(square.perimeter(5), 20)

    def testZeroSides(self):
        self.assertEqual(square.perimeter(0), 0)

    def testBigSides(self):
        self.assertEqual(square.perimeter(20_000), 80_000)