import unittest

# Import our functions for testing
import circle
import square
import rectangle
import triangle


class TestGeometricMethods(unittest.TestCase):
	kDigitsOfPrecision = 14
	def test_circumference_length(self):
		self.assertAlmostEqual(circle.perimeter(0.5), 3.1415926535897932, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(circle.perimeter(0), 0, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(circle.perimeter(6.18), 38.8300851983698444, TestGeometricMethods.kDigitsOfPrecision)

	def test_circle_area(self):
		self.assertAlmostEqual(circle.area(4.2), 55.4176944093239527, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(circle.area(0), 0, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(circle.area(22.8), 1633.12552504211811, TestGeometricMethods.kDigitsOfPrecision)

	def test_square_perimeter(self):
		self.assertAlmostEqual(square.perimeter(5), 20, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(square.perimeter(0), 0, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(square.perimeter(12.5), 50, TestGeometricMethods.kDigitsOfPrecision)

	def test_square_area(self):
		self.assertAlmostEqual(square.area(1.3), 1.69, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(square.area(0), 0, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(square.area(6.13785746), 37.6732941992776516, TestGeometricMethods.kDigitsOfPrecision)

	def test_rectangle_perimeter(self):
		self.assertAlmostEqual(rectangle.perimeter(1, 2.28), 6.56, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(rectangle.perimeter(0, 4), 8, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(rectangle.perimeter(1.5, 2.5), 8, TestGeometricMethods.kDigitsOfPrecision)

	def test_rectangle_area(self):
		self.assertAlmostEqual(rectangle.area(1, 2.28), 2.28, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(rectangle.area(0, 4), 0, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(rectangle.area(1.5, 4.2), 6.3, TestGeometricMethods.kDigitsOfPrecision)

	def test_triangle_perimeter(self):
		self.assertAlmostEqual(triangle.perimeter(1, 2, 3), 6, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(triangle.perimeter(0, 4, 5), 9, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(triangle.perimeter(1.5, 2.5, 3.5), 7.5, TestGeometricMethods.kDigitsOfPrecision)

	def test_triangle_area(self):
		self.assertAlmostEqual(triangle.area(1, 2), 1, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(triangle.area(6, 3), 9, TestGeometricMethods.kDigitsOfPrecision)
		self.assertAlmostEqual(triangle.area(1.5, 2.2), 1.65, TestGeometricMethods.kDigitsOfPrecision)


if __name__ == '__main__':
	unittest.main()
