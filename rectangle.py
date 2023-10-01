from typing import Union


def area(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Принимает длины сторон прямоугольника и возвращает площадь прямоугольника

    :param a: длина прямоугольника
    :param b: ширина прямоугольника
    :return: площадь прямоугольника со сторонами a и b
    """
    return a * b


def perimeter(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Принимает длины сторон прямоугольника и возвращает периметр прямоугольника

    :param a: длина прямоугольника
    :param b: ширина прямоугольника
    :return: периметр прямоугольника со сторонами a и b
    """
    return (a + b) * 2
