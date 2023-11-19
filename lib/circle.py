import math


def area(r):
    """
    Calculates the area of circle
    :param r: circle radius value
    :type r: int or float
    :rtype: float
    :return: math.pi * r * r - area of a circle
    """
    return math.pi * r * r


def perimeter(r):
    """
    Calculates the perimeter of circle
    :param r: circle radius value
    :type r: int or float
    :rtype: float
    :return: 2 * math.pi * r - perimeter of a circle
    """
    return 2 * math.pi * r

