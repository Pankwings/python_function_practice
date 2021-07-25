import unittest
from math import pi
from circle import circle_area

class testcirclearea(unittest.TestCase):
    def test_area(self):
        # Test the area of circle radius >=0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1),(2.1*2.1*pi))
    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)
    def test_types(self):
        # Make sure type error is raised when input is not a real number.
        self.assertRaises(TypeError, circle_area, 2+3j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, 'radius')


