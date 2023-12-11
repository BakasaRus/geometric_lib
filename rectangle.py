
def area(a, b):
    '''Принимает стороны прямоугольника a и b, возвращает площадь прямоугольника'''
    if (a < 0 or b < 0):
        raise ValueError
    return a * b


def perimeter(a, b):
    '''Принимает стороны прямоугольника а и b, возвращает периметр прямоугольника'''
    if (a < 0 or b < 0):
        raise ValueError
    return 2 * (a + b)
