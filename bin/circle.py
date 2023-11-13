import math


'''
area(r: float): float
this function calculates circle area by it's radius
'''
def area(r):
    if not (isinstance(r, float) or isinstance(r, int)):
        raise TypeError("ERROR: incorrect arguments passed")
    if r < 0:
        raise ValueError("ERROR: circle radius can't be negative!")
    return math.pi * r * r


'''
perimeter(r: float): float
this function calculates circumference length by radius of circle
'''
def perimeter(r):
    if not (isinstance(r, float) or isinstance(r, int)):
        raise TypeError("ERROR: incorrect arguments passed")
    if r < 0:
        raise ValueError("ERROR: circle radius can't be negative!")
    return 2 * math.pi * r

