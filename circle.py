import math


def area(r):
    '''Receives radius of the circle and returns its area.'''
    if (type(r) == str):
        raise ValueError('Input must be integer!')
    if (r <= 0):
        raise ValueError('All lengths must be positive!')
    return math.pi * r * r


def perimeter(r):
    '''Receives radius of the circle and returns its perimeter.'''
    if (type(r) == str):
        raise ValueError('Input must be integer!')
    if (r <= 0):
        raise ValueError('All lengths must be positive!')
    return 2 * math.pi * r
