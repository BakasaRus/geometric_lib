import math

def area(r):
    '''
    Вычисление площади круга
    Параметр:
        r(int/float) - радиус круга
        math.pi(float) - число пи
    Возвращаемое значение:
        math.pi * r * r(float) - Площадь круга
    Пример вызова:
        area(10) = 314.1592653589793
    '''
    if(type(r) == str):
        raise(TypeError)
    return math.pi * r * r
#check
def perimeter(r):
    '''
    Вычисление периметра
    Параметр:
        r(int/float) - радиус круга
        math.pi(float) - число пи
    Вовзращаемое значение:
        2 * math.pi * r(float) - Периметр круга
    Пример вызова:
        perimeter(10) = 62.83185307179586
    '''
    if(type(r) == str):
        raise(TypeError)
    return 2 * math.pi * r