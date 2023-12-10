def area(a):
    '''
    Вычисление площади квадрата
    Параметр:
        a(int/float) - сторона квадрата
    Возвращаемое значение:
        a * a(int/float) - площадь квадрата
    Пример вызова:
        area(10) = 100
    '''
    if(type(a) == str):
        raise(TypeError)
    return a * a

def perimeter(a):
    '''
    Вычисление периметра квадрата
    Параметры:
        a(int/float) - сторона квадрата
    Возвращаемое значение:
        4 * a(int/float) - площадь квадрата
    Пример вызова:
        perimeter(10) = 40
    '''
    if(type(a) == str):
        raise(TypeError)
    return 4 * a