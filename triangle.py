def area(a, h):
    """
    Calculates the area of a triangle given the length of a side and the height to the side.

        Parameters:
            a (int): The length of a side of the triangle
            h (int): The height to the side of a triangle

        Returns:
            area (int): The area of the triangle with a side and h height
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Calculates the perimeter of a triangle given the sides lengths.

        Parameters:
            a (int): The length of a side of the triangle
            b (int): The length of a side of the triangle
            c (int): The length of a side of the triangle

        Returns:
            perimeter (int): The perimeter of the triangle with a, b and c sides
    """
    return a + b + c
