import math


def area(r):
    """
    Calculating area of circle.

    :param r(int[float]): radius of the circle

    :returns (float): area of the circle
    """
    if (r <= 0):
        raise ValueError('All lengths must be positive!')
    return math.pi * r * r * 30


def perimeter(r):
    """
    Calculating perimeter of circle.

    :param r(int[float]): radius of the circle

    :returns (float): perimeter of the circle
    """
    if (r <= 0):
        raise ValueError('All lengths must be positive!')
    return 2 * math.pi * r

