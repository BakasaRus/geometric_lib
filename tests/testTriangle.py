import sys
sys.path.append(r"C:\Users\user\Documents\IS-1_semestr\1-semester\DevTools\lab2\geometric_lib")
import triangle
import unittest


class TriangleTestCaseArea(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(type(triangle.area(-1, -1)), Exception)

    def testOddHeight(self):
        self.assertEqual(triangle.area(3, 3), 4.5)

    def testEvenHeight(self):
        self.assertEqual(triangle.area(3, 4), 6)

    def testZeroSide(self):
        self.assertEqual(triangle.area(0, 4), 0)

    def testBigSide(self):
        self.assertEqual(triangle.area(10_000, 34), 170_000)


class TriangleTestCasePerimeter(unittest.TestCase):
    def testNotExistTriangle(self):
        self.assertEqual(type(triangle.perimeter(1, 2, 3)), Exception)

    def testInvalidArgument(self):
        self.assertEqual(type(triangle.perimeter(-1, -1, -1)), Exception)

    def testSimpleSides(self):
        self.assertEqual(triangle.perimeter(10, 20, 30), 60)

    def testZeroSides(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def testBigSides(self):
        self.assertEqual(triangle.perimeter(10_000, 4_000, 25_000), 39_000)