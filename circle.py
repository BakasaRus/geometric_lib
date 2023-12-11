import math

def area(r):
    '''Принимает радиус круга r, возвращает его площадь'''
    if r <= 0:
        return -1
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус круга r, возвращает его периметр'''
    if r <= 0:
        return -1
    return 2 * math.pi * r
