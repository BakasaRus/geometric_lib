import unittest
import config
import square

class TestSquareMethods(unittest.TestCase):
	def test_square_perimeter_typeerror(self):
		self.assertRaises(TypeError, square.perimeter, 'b')
	def test_square_perimeter_valueerror(self):
		self.assertRaises(ValueError, square.perimeter, -1)
	def test_square_perimeter_int(self):
		self.assertEqual(square.perimeter(0), 0)
	def test_square_perimeter_float(self):
		self.assertAlmostEqual(square.perimeter(12.5), 50, config.kDigitsOfPrecision)

	def test_square_area_typeerror(self):
		self.assertRaises(TypeError, square.area, 'b')
	def test_square_area_valueerror(self):
		self.assertRaises(ValueError, square.area, -1)
	def test_square_area_int(self):
		self.assertEqual(square.area(0), 0)
	def test_square_area_float(self):
		self.assertAlmostEqual(square.area(6.13785746), 37.6732941992776516, config.kDigitsOfPrecision)
