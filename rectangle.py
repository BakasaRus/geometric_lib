def area(a, b): 
    '''
    Returns the area of a rectangle with the specified sides

        Parameters:
            a (int / float): length of the first side of the rectangle (length)
            b (int / float): length of the second side of the rectangle (width)

        Returns value:
            area (int / float): the area of a rectangle with sides a and b
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('Not numbers are passed to the function')
    
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('Not numbers are passed to the function')

    if (a <= 0 or b <= 0):
        raise ValueError('Incorrect input')

    return a * b 

def perimeter(a, b): 
    '''
    Returns the perimeter of a rectangle with the specified sides

        Parameters:
            a (int / float): length of the first side of the rectangle (length)
            b (int / float): length of the second side of the rectangle (width)

        Returns value:
            perimeter (int / float): the perimeter of a rectangle with sides a and b
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('Not numbers are passed to the function')
    
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('Not numbers are passed to the function')

    if (a <= 0 or b <= 0):
        raise ValueError('Incorrect input')
    return (a + b) * 2 