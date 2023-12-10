def area(a, h):
    '''Принимает длины стороны треугольника и высоты, проведённой к ней, возвращает его площадь'''
    if a <= 0 or h <= 0:
        return -1
    return a * h / 2


def perimeter(a, b, c):
    '''Принимает длины трёх сторон треугольника, возвращает его периметр'''
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    if max(a, b, c) >= (a + b + c - max(a, b, c)):
        return -1
    return a + b + c
