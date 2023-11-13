def area(a, b):
    '''Принимает 2 числа - a, b, возвращает площадь прямоугольника со сторонами a, b'''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError
    if a <= 0 or b <= 0:
        raise ValueError
    return a * b

def perimeter(a, b):
    '''Принимает 2 числа - a, b, возвращает периметр прямоугольника со сторонами a, b'''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError
    if a <= 0 or b <= 0:
        raise ValueError
    return a * 2 + b * 2
