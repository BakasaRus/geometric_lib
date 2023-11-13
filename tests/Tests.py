import unittest
import testCircle
import testSquare
import testTriangle
import testRectangle

circleArea = testCircle.CircleTestCaseArea
circlePerimeter = testCircle.CircleTestCasePerimeter

squareArea = testSquare.SquareTestCaseArea
squarePerimeter = testSquare.SquareTestCasePerimeter

triangleArea = testTriangle.TriangleTestCaseArea
trianglePerimeter = testTriangle.TriangleTestCasePerimeter

rectangleArea = testRectangle.RectangleTestCaseArea
rectanglePerimeter = testRectangle.RectangleTestCasePerimeter

if __name__ == "__main__":
    unittest.main()
