import math
from typing import Union


def area(r: Union[int, float]) -> Union[int, float]:
    """
    Принимает радиус круга и возвращает площадь круга

    :param r: радиус круга
    :return: площадь круга
    """
    return math.pi * r * r


def perimeter(r: Union[int, float]) -> Union[int, float]:
    """
    Принимает радиус круга и возвращает периметр круга

    :param r: радиус круга
    :return: периметр круга
    """
    return 2 * math.pi * r

