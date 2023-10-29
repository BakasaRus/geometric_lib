import unittest
import circle


class CircleTestCase(unittest.TestCase):

    def test_area_first(self):
        res = circle.area(10)
        self.assertEqual(314.1592653589793, res)

    def test_area_second(self):
        res = circle.area(3)
        self.assertEqual(28.274333882308138, res)

    def test_perimeter_first(self):
        res = circle.perimeter(100)
        self.assertEqual(628.3185307179587, res)

    def test_perimeter_second(self):
        res = circle.perimeter(200)
        self.assertEqual(1256.6370614359173, res)

    @classmethod
    def setUpClass(cls):
        print(f'Testing {cls.__name__}...')

    @classmethod
    def tearDownClass(cls):
        print(f'Tested {cls.__name__}')


if __name__ == '__main__':
    unittest.main()
