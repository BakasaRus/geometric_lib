def area(a):
    """
    Calculating area of square.

    :param a(int[float]): length of the side of the square

    :returns (int[float]): area of the square
    """
    if (a <= 0):
        raise ValueError('All lengths must be positive!')
    return a * a

def test_func():
    """
    Test function.

    :returns: nothing
    """
    pass

def perimeter(a):
    """
    Calculating perimeter of square.

    :param a(int[float]): length of the side of the square

    :returns (int | float): perimeter of the square
    """
    if (a <= 0):
        raise ValueError('All lengths must be positive!')
    return 4 * a
