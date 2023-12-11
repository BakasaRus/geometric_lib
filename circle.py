import math


def area(r):
    '''
        Calculates the area of a circle with radius r
            Parameters:
                r (int/float): radius of the circle

            Returns:
                area (int/float): the area of the circle with radius r
    '''
    if (isinstance(r, (float, int)) and r >= 0):
        return math.pi * r * r
    else:
        raise Exception


def perimeter(r):
    '''
        Calculates the perimeter of a circle with radius r
            Parameters:
                r (int/float): radius of the circle

            Returns:
                perimeter (int/float): the perimeter of the circle with radius r
    '''
    if (isinstance(r, (float, int)) and r >= 0):
        return math.pi * r * 2
    else:
        raise Exception
