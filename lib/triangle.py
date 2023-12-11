def area(a, h):
    '''Принимает 2 числа - a, h, возвращает площадь треугольника с высотой h и основанием a'''
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError
    if a <= 0 or h <= 0:
        raise ValueError
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает 3 числа - a, b, c, возвращает площадь треугольника со сторонами a, b, c'''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError
    return a + b + c
