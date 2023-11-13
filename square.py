def area(a):
    '''
        Calculates the area of a square with side a
            Parameters:
                a (int/float): side of the square

            Returns:
                area (int/float): the area of the square with side a
    '''
    if (isinstance(a, (float, int)) and a >= 0):
        return a * a
    else:
        raise Exception


def perimeter(a):
    '''
        Calculates the perimeter of a square with side a
            Parameters:
                a (int/float): side of the square

            Returns:
                perimeter (int/float): the perimeter of the square with side a
    '''

    if (isinstance(a, (float, int)) and a >= 0):
        return 4 * a
    else:
        raise Exception
