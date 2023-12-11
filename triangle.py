
def area(a, h):
    '''Принимает сторону треугольника a и высоту h, возвращает площадь треугольника'''
    if (a < 0 or h < 0):
        raise ValueError
    return a * h / 2


def perimeter(a, b, c):
    '''Принимает сторону треугольника а и высоту h, возвращает периметр треугольника'''
    if (a < 0 or b < 0 or c < 0):
        raise ValueError
    return a + b + c
