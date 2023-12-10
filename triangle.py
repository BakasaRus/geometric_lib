def area(a, h):
    '''
    Вычисление площади треугольника
    Параметры:
        h, a(int/float) - высота и сторона(основание)
    Возвращаемое значение:
        a * h / 2(int/float) - площадь треугольника
    Пример вызова:
        area(2, 4) = 4
    '''
    if(type(a) == str or type(h) == str):
        raise(TypeError)
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Вычисление периметра треугольника
    Параметры:
        a, b, c(int/float) - 3 стороны треугольника
    Возвращаемое значение:
        a + b + c(int/float) - площадь треугольника
    Пример вызова:
        perimeter(3, 4, 5) = 12
    ''' 
    if(type(a) == str or type(b) == str or type(c) == str):
        raise(TypeError)
    return a + b + c 