import math

def checkValue(r):
    if (r < 0):
        raise ValueError("Given negative value for radius: ", r)

def area(r):
    '''
    Возвращает площадь круга в зависимости от его радиуса

        Параметры:
            r (int/float): радиус круга

        Возвращаемое значение:
            area (float): площадь круга с радиусом r
    '''
    checkValue(r)
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга в зависимости от его радиуса

        Параметры:
            r (int/float): радиус круга

        Возвращаемое значение:
            perimeter (float): периметр круга с радиусом r
    '''
    checkValue(r)
    return 2 * math.pi * r
