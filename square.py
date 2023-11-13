
def area(a):
    '''Receives length of the side and returns area of the square.'''
    if (type(a) == str):
        raise ValueError('Input must be integer!')
    if (a <= 0):
        raise ValueError('All lengths must be positive!')
    return a * a


def perimeter(a):
    '''Receives length of the side and returns perimetr of the square.'''
    if (type(a) == str):
        raise ValueError('Input must be integer!')
    if (a <= 0):
        raise ValueError('All lengths must be positive!')
    return 4 * a
