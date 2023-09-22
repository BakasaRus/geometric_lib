def area(a, h):
    '''
    Calculates the area of triangle
    :param a: size of the side of the triangle to which the height is build
    :type a: int or float
    :param h: height of triangle
    :type h: int or float
    :rtype: int or float
    :return: a * h / 2 - area of triangle
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Calculates the perimeter of triangle
    :param a: size of the first side of the triangle
    :type a: int or float
    :param b: size of the second side of the triangle
    :type b: int or float
    :param c: size of the third side of the triangle
    :type c : int or float
    :rtype: int or float
    :return: a + b + c - perimeter of triangle
    '''
    return a + b + c
