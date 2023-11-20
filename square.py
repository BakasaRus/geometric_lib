def area(a):
    '''
    Returns the area of a square with the specified side

        Parameters:
            a (int / float): length of the side of the square

        Returns value:
            area (int / float): the area of a square with side a 
    '''
    if (a <= 0):
        raise ValueError('Incorrect input')

    return a * a


def perimeter(a):
    '''
    Returns the perimeter of a square with the specified side

        Parameters:
            a (int / float): length of the side of the square

        Returns value:
            perimeter (int / float): the perimeter of a square with side a 
    '''
    if (a <= 0):
        raise ValueError('Incorrect input')
    
    return 4 * a
