'''
area(a: float, b: float): float
this function calculates area of rectangle by it's two sides
'''
def area(a, b):
    if not (isinstance(a, float) or isinstance(a, int)) or not\
           (isinstance(b, float) or isinstance(b, int)):
        raise TypeError("ERROR: incorrect arguments passed")
    if a < 0 or b < 0:
        raise ValueError("ERROR: rectangle sides can't be negative!")
    return a * b

'''
perimeter(a: float, b: float): float
this function calculates perimeter of rectangle by it's two sides
'''
def perimeter(a, b):
    if not (isinstance(a, float) or isinstance(a, int)) or not\
           (isinstance(b, float) or isinstance(b, int)):
        raise TypeError("ERROR: incorrect arguments passed")
    if a < 0 or b < 0:
        raise ValueError("ERROR: rectangle sides can't be negative!")
    return 2 * (a + b)
