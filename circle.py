import math
import unittest

def area(r):
    '''
    Takes a number r and returns the area of a circle with radius r.
    Example: area(3) = pi * 9
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Takes a number r and returns the circumference of a circle with radius r.
    Example: perimeter(3) = pi * 6
    '''
    return 2 * math.pi * r
