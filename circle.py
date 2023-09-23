import math


def area(r):
    """
    Calculating area of circle.

    :param r(int[float]): radius of the circle

    :returns (float): area of the circle
    """
    return math.pi * r * r


def perimeter(r):
    """
    Calculating perimeter of circle.

    :param r(int[float]): radius of the circle

    :returns (float): perimeter of the circle
    """
    return 2 * math.pi * r

