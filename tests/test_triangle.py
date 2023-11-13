import unittest
import config
import triangle

class TestTriangleMethods(unittest.TestCase):
	def test_triangle_perimeter_typeerror(self):
		self.assertRaises(TypeError, triangle.perimeter, 'b', 1, 1)
	def test_triangle_perimeter_valueerror(self):
		self.assertRaises(ValueError, triangle.perimeter, -1, 1, 2)
	def test_triangle_perimeter_int(self):
		self.assertEqual(triangle.perimeter(3, 4, 5), 12)
	def test_triangle_perimeter_float(self):
		self.assertAlmostEqual(triangle.perimeter(1.5, 2.5, 3.5), 7.5, config.kDigitsOfPrecision)

	def test_triangle_area_typeerror(self):
		self.assertRaises(TypeError, triangle.area, 'b', 1)
	def test_triangle_area_valueerror(self):
		self.assertRaises(ValueError, triangle.area, -1, 1)
	def test_triangle_area_int(self):
		self.assertEqual(triangle.area(6, 3), 9)
	def test_triangle_area_float(self):
		self.assertAlmostEqual(triangle.area(1.5, 2.2), 1.65, config.kDigitsOfPrecision)
