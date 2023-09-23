import math


def area(r):
    """Returns circle area with given radius.

    :param r: circle radius
    :type r: int|float

    :rtype: float
    :return: circle area
    """
    return math.pi * r * r


def perimeter(r):
    """Returns circle perimetr with given radius

    :param r: circle radius
    :type r: int|float

    :rtype: float
    :return: circle perimeter
    """
    return 2 * math.pi * r

