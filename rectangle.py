def area(a, b): 
    '''
    Вычисление площади прямоугольника
    Параметры:
        a, b(int/float) - длина и ширина прямоугольника
    Возвращаемое значение:
        a * b(int/float) - площадь прямоугольника
    Пример вызова:
        area(2, 3) = 6
    '''
    if(type(a) == str or type(b) == str):
        raise(TypeError)
    return a * b 

def perimeter(a, b): 
    '''
    Вычисление периметра прямоугольника
    Параметры:
        a, b(int/float) - длина и ширина прямоугольника
    Возвращаемое значение:
        2 * (a + b) (int/float) - периметр прямоугольника
    Пример вызова:
        perimeter(2, 3) = 10
    '''
    if(type(a) == str or type(b) == str):
        raise(TypeError)
    return 2*(a + b) 