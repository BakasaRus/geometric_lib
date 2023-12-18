def area(a, b):
    '''Receives length of 2 sides and returns area of the rectangle'''
    if (type(a) == str or type(b) == str):
        raise ValueError('Input must be integer!')
    if(a < 0 or b < 0):
        raise ValueError('All lengths must be positive!')

    return a * b

def perimeter(a, b):
    '''Receives length of 2 sides and returns perimeter of the rectangle.'''
    if (type(a) == str or type(b) == str):
        raise ValueError('Input must be integer!')
    if (a < 0 or b < 0):
        raise ValueError('All lengths must be positive!')

    return 2 * (a + b)