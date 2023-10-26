
def area(a):
    '''
        Возвращает площадь квадрата с заданой стороной

            Параметры:
                a (float): сторона квадрата
            Возвращаемое значение:
                S (float): площадь квадрата
    '''
    
    if type(a) not in [int, float]:
        raise TypeError("Стороны должны быть рациональными числами")

    if a < 0:
        raise ValueError("Стороны должны быть положительными") 
    
    return a * a


def perimeter(a):
    '''
        Возвращает периметр квадрата с заданой стороной

            Параметры:
                a (float): сторона квадрата
            Возвращаемое значение:
                P (float): периметр квадрата
    '''

    if type(a) not in [int, float]:
        raise TypeError("Стороны должны быть рациональными числами")

    if a < 0:
        raise ValueError("Стороны должны быть положительными") 
    
    return 4 * a