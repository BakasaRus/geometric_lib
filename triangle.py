def area(a, h):
    '''
        Calculates the area of a triangle with side a and height h
            Parameters:
                a (int/float): side of the triangle
                h (int/float): height of the triangle

            Returns:
                area (int/float): the area of a triangle with side a and height h
    '''
    if (isinstance(a, (float, int)) and isinstance(h, (float, int)) and a >= 0 and h >= 0):
        return a * h / 2
    else:
        raise Exception


def perimeter(a, b, c):
    '''
        Calculates the perimeter of a triangle with sides a, b and c
            Parameters:
                a (int/float): first side of the rectamgle
                b (int/float): second side of the rectamgle
                c (int/float): third side of the rectamgle

            Returns:
                perimeter (int/float): the perimeter of the triangle with sides a, b and c
    '''
    if (isinstance(a, (float, int)) and isinstance(b, (float, int)) and isinstance(c, (
    float, int)) and a >= 0 and b >= 0 and a >= 0):
        return a + b + c
    else:
        raise Exception
