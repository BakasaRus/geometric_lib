def area(a, h):

    '''
        Возвращает площадь треугольника с задаными высотой и основанием

            Параметры:
                a (float): основание треугольника
                h (float): высота треугольника
            Возвращаемое значение:
                S (float): площадь треугольника
    '''

    if (type(a) not in [int, float]) or (type(h) not in [int, float]):
        raise TypeError("Числа должны быть рациональными")

    if a < 0 or h < 0:
        raise ValueError("Числа должны быть положительными") 
    
    return a * h / 2 

def perimeter(a, b, c):
    '''
        Возвращает периметр треугольника с задаными сторонами

            Параметры:
                a (float): первая сторона треугольника
                b (float): вторая сторона треугольника
                c (float): третья сторона треугольника
            Возвращаемое значение:
                P (float): периметр треугольника
    '''

    if (type(a) not in [int, float]) or (type(b) not in [int, float]) or (type(c) not in [int, float]):
        raise TypeError("Стороны должны быть рациональными числами")

    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны должны быть положительными") 

    return a + b + c