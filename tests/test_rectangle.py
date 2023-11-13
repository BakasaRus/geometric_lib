import unittest
import config
import rectangle

class TestRectangleMethods(unittest.TestCase):
	def test_rectangle_perimeter_typeerror(self):
		self.assertRaises(TypeError, rectangle.perimeter, 'b', 1)
	def test_rectangle_perimeter_vlaueerror(self):
		self.assertRaises(ValueError, rectangle.perimeter, -1, 1)
	def test_rectangle_perimeter_int(self):
		self.assertEqual(rectangle.perimeter(0, 4), 8)
	def test_rectangle_perimeter_float(self):
		self.assertAlmostEqual(rectangle.perimeter(1.5, 2.5), 8, config.kDigitsOfPrecision)

	def test_rectangle_area_typeerror(self):
		self.assertRaises(TypeError, rectangle.area, 'b', 1)
	def test_rectangle_area_valueerror(self):
		self.assertRaises(ValueError, rectangle.area, -1, 1)
	def test_rectangle_area_int(self):
		self.assertEqual(rectangle.area(0, 4), 0)
	def test_rectangle_area_float(self):
		self.assertAlmostEqual(rectangle.area(1.5, 4.2), 6.3, config.kDigitsOfPrecision)
