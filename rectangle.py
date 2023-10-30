def area(a, b):
    """
    Calculating area of rectangle.

    :param a(int[float]): first side of the rectangle
    :param b(int[float]): second side of the rectangle

    :returns (float): area of the rectangle
    """
    if (a <= 0 or b <= 0):
        raise ValueError('All lengths must be positive!')
    return a * b

def perimeter(a, b):
    """
    Calculating perimeter of rectangle.

    :param a(int[float]): first side of the rectangle
    :param b(int[float]): second side of the rectangle

    :returns (float): perimeter of the rectangle
    """
    if (a <= 0 or b <= 0):
        raise ValueError('All lengths must be positive!')
    return (a + b) * 2
