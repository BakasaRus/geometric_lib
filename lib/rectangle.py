def area(a, b):
    '''
    Calculates the area of rectangle
    :param a: size of the side of the rectangle (first side)
    :type a: int or float
    :param b: size of the side of the rectangle (adjacent to the first side)
    :type b: int or float
    :rtype: int or float
    :return: a*b - area of the rectangle
    '''
    return a * b


def perimeter(a, b):
    '''
    Calculates the perimeter of rectangle
    :param a: size of the side of the rectangle (first side)
    :type a: int or float
    :param b: size of the side of the rectangle (adjacent to the first side)
    :type b: int or float
    :rtype: int or float
    :return: 2*(a+b) - perimeter of the rectangle
    '''
    return 2 * (a + b)
