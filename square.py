def checkValues(a):
    if (a < 0):
        raise ValueError("Given negative value for square side: ", a)

def area(a):
    '''
    Возвращает площадь квадрата в зависимости от длины его стороны

        Параметры:
            a (int/float): длина стороны квадрата

        Возвращаемое значение:
            area (int/float): площадь квадрата со стороной a
    '''
    checkValues(a)
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата в зависимости от длины его стороны

        Параметры:
            a (int/float): длина стороны квадрата

        Возвращаемое значение:
            area (int/float): периметр квадрата со стороной a
    '''
    checkValues(a)
    return 4 * a
