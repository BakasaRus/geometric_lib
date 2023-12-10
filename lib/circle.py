import math


def area(r):
    '''
    Принимает одно число: радиус окружности.
    
    возвращает приближительное значение площади круга в типе данных float
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает одно число: радиус окружности.
    
    возвращает приближительное значение длины круга в типе данных float
    '''
    return 2 * math.pi * r
