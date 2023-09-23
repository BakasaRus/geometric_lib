
def area(a, h):
    """Return area of triangle with given params

    :param a: base of triangle
    :type a: int|float

    :param h: height of triangle
    :type h: int|float

    :rtype: int|float
    :return: area of triangle
    """
    return a * h / 2


def perimeter(a, b, c):
    """Return perimeter of triangle with given params

    :param a: first side of triangle
    :type a: int|float

    :param b: second side of triangle
    :type b: int|float

    :param c: third side of triangle
    :type c: int|float

    :rtype: int|float
    :return: perimeter of triangle
    """
    return a + b + c
