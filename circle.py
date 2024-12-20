import math


def area(r):
    """
    Calculates the area of a circle given the radius.

        Parameters:
            r (int): The radius of the circle

        Returns:
            area (int): The area of the circle with r radius
    """
    return math.pi * r * r


def perimeter(r):
    """
    Calculates the perimeter of a circle given the radius.

        Parameters:
            r (int): The radius of the circle

        Returns:
            perimeter (int): The perimeter of the circle with r radius
    """
    return 2 * math.pi * r

