
def area(a):
    '''Принимает сторону квадрата a, возвращает площадь квадрата'''
    if (a < 0):
        raise ValueError
    return a * a


def perimeter(a):
    '''Принимает сторону квадрата а, возвращает периметр квадрата'''
    if (a < 0):
        raise ValueError
    return 4 * a
