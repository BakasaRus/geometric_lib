'''
area(a: float): float
this function calculates area of square by it's side
'''
def area(a):
    if not (isinstance(a, float) or isinstance(a, int)):
        raise TypeError("ERROR: incorrect arguments passed")
    if a < 0:
        raise ValueError("ERROR: square side can't be negative!")
    return a * a

'''
perimeter(a: float): float
this function calculates perimeter of square by it's side
'''
def perimeter(a):
    if not (isinstance(a, float) or isinstance(a, int)):
        raise TypeError("ERROR: incorrect arguments passed")
    if a < 0:
        raise ValueError("ERROR: square side can't be negative!")
    return 4 * a
