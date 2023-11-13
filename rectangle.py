def area(a, b):
    '''
        Calculates the area of a rectangle with sides a and b
            Parameters:
                a (int/float): first side of the rectamgle
                b (int/float): second side of the rectamgle
                
            Returns:
                area (int/float): the area of the rectangle with sides a and b
    '''
    if (isinstance(a, (float, int)) and isinstance(b, (float, int)) and a >= 0 and b >= 0):
        return a * b
    else:
        raise Exception


def perimeter(a, b):
    '''
        Calculates the perimeter of a rectangle with sides a and b
            Parameters:
                a (int/float): first side of the rectamgle
                b (int/float): second side of the rectamgle

            Returns:
                perimeter (int/float): the perimeter of the rectangle with sides a and b
    '''
    if (isinstance(a, (float, int)) and isinstance(b, (float, int)) and a >= 0 and b >= 0):
        return (a + b) * 2
    else:
        raise Exception
