def area(a, h):
    '''Receives length of the side and height of the triangle and returns its area.'''
    if (type(a) == str or type(h) == str):
        raise ValueError('Input must be integer!')
    if (a <= 0 or h <= 0):
        raise ValueError('All lengths must be positive!')
    return a * h / 2

def perimeter(a, b, c):
    '''Receives length of 3 sides of the triangle and returns its perimeter.'''
    if (type(a) == str or type(b) == str or type(c) == str):
        raise ValueError('Input must be integer!')
    if (a <= 0 or b <= 0 or c <= 0):
        raise ValueError('All lengths must be positive!')
    if (a + b <= c or a + c <= b or b + c <= a):
        raise ValueError('The triangle inequality does not hold!')
    return a + b + c