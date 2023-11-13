import sys
sys.path.append(r"C:\Users\user\Documents\IS-1_semestr\1-semester\DevTools\lab2\geometric_lib")
import square
import unittest


class SquareTestCaseArea(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(type(square.area(-1)), Exception)

    def testSimpleSides(self):
        self.assertEqual(square.area(3), 9)

    def testZeroSides(self):
        self.assertEqual(square.area(0), 0)

    def testBigSides(self):
        self.assertEqual(square.area(10_000), 100_000_000)


class SquareTestCasePerimeter(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(type(square.perimeter(-1)), Exception)

    def testSimpleSides(self):
        self.assertEqual(square.perimeter(5), 20)

    def testZeroSides(self):
        self.assertEqual(square.perimeter(0), 0)

    def testBigSides(self):
        self.assertEqual(square.perimeter(20_000), 80_000)