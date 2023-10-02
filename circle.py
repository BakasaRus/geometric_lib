import math

def area(r):
    '''
    Returns the area of a circle with with the specified radius

        Parameters:
            r (int / float): circle radius

        Returns value:
            area (int / float): the area of a circle with radius r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Returns the length of a circle with with the specified radius

        Parameters:
            r (int / float): circle radius

        Returns value:
            perimeter (int / float): the length of a circle of a circle of radius r
    '''
    return 2 * math.pi * r
