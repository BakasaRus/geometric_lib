def area(a, h):
    """
    Calculating area of triangle.

    :param a(int[float]): length of one side of the triangle
    :param h(int[float]): appropriate height of the triangle

    :returns (float): area of the triangle
    """
    return a * h / 2

def perimeter(a, b, c):
    """
    Calculating perimeter of triangle

    :param a(int[float]): first side of the triangle
    :param b(int[float]): second side of the triangle
    :param c(int[float]): third side of the triangle

    :returns (float): perimeter of the triangle
    """
    return a + b + c