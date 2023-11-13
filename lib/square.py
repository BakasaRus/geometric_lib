def area(a):
    '''Принимает число a, возвращает площадь квадрата со стороной a'''
    if not isinstance(a, (int, float)):
        raise TypeError
    if a <= 0:
        raise ValueError
    return a * a


def perimeter(a):
    '''Принимает число a, возвращает периметр квадрата со стороной a'''
    if not isinstance(a, (int, float)):
        raise TypeError
    if a <= 0:
        raise ValueError
    return 4 * a
