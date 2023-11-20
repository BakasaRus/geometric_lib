def area(a, h):
    '''
    Returns the area of a triangle with the specified side and height drawn to that side

        Parameters:
            a (int / float): length of the side of the square

        Returns value:
            area (int / float): the area of a triangle with the specified side and height drawn to that side 
    '''
    if a <= 0 or h <= 0:
        raise ValueError('Incorrect input')
    
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Returns the perimeter of a triangle with the specified side and height drawn to that side

        Parameters:
            a (int / float): length of the first side of the square
            b (int / float): length of the second side of the square
            c (int / float): length of the third side of the square

        Returns value:
            perimeter (int / float): the perimeter of a triangle with the specified side and height drawn to that side 
    '''
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Incorrect input')
    
    if a >= b + c or b >= a + c or c >= a + b:
        raise ValueError('There is no such triangle')
    
    return a + b + c 