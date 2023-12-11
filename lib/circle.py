import math

def area(r):
    '''Принимает число r, возвращает площадь круга радиусом r'''
    if not isinstance(r, (int, float)):
        raise TypeError
    if r <= 0:
        raise ValueError
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r, возвращает длину окружности радиусом r'''
    if not isinstance(r, (int, float)):
        raise TypeError
    if r <= 0:
        raise ValueError
    return 2 * math.pi * r
