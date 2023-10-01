from typing import Union


def area(a: Union[int, float], h: Union[int, float]) -> Union[int, float]:
    """
    Принимает длину основания и высоту, перпендикулярную основанию, треугольника и
    возвращает площадь треугольника

    :param a: основание треугольника
    :param h: высота треугольника
    :return: площадь треугольника
    """
    return a * h / 2 

def perimeter(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Union[int, float]:
    """
    Принимает длину сторон треугольника и возвращает периметр треугольника

    :param a: 1-ая сторона треугольника
    :param b: 2-ая сторона треугольника
    :param c: 3-ая сторона треугольника
    :return: периметр треугольника
    """
    return a + b + c
