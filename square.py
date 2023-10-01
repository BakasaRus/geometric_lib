from typing import Union


def area(a: Union[int, float]) -> Union[int, float]:
    """
    Принимает длину стороны квадрата и возвращает площадь квадрата

    :param a: сторона квадрата
    :return: площадь квадрата со стороной a
    """
    return a * a


def perimeter(a: Union[int, float]) -> Union[int, float]:
    """
    Принимает длину стороны квадрата и возвращает периметр квадрата

    :param a: сторона квадрата
    :return: периметр квадрата со стороной a
    """
    return 4 * a
