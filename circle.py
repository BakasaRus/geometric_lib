import math


def area(r):
    '''Принимает радиус круга r, возвращает площадь круга'''
    if (r < 0):
        raise ValueError
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус круга r, возвращает периметр круга'''
    if (r < 0):
        raise ValueError
    return 2 * math.pi * r
