import math


def area(r):
    '''
        Возвращает площадь круга с заданым радиусом

            Параметры:
                r (float): радиус круга
            Возвращаемое значение:
                S (float): площадь круга
    '''
    if type(r) not in [int, float]:
        raise TypeError("Радиус должен быть рациональным")

    if r < 0:
        raise ValueError("Радиус должен быть положительным") 
    
    return math.pi * r * r


def perimeter(r):
    '''
        Возвращает периметр круга с заданым радиусом

            Параметры:
                r (float): радиус круга
            Возвращаемое значение:
                P (float): радиус круга
    '''

    if type(r) not in [int, float]:
        raise TypeError("Радиус должен быть рациональным")

    if r < 0:
        raise ValueError("Радиус должен быть положительным") 
    
    return 2 * math.pi * r