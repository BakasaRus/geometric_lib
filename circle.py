import math


def area(r):
    '''
        Принимает число r и возвращает площадь круга с радиусом r.
        Пример: area(3) = pi * 9
    '''
    return math.pi * r * r


def perimeter(r):
    '''
        Принимает число r и возвращает длину окружности с радиусом r.
        Пример: perimeter(3) = pi * 6
    '''
    return 2 * math.pi * r

