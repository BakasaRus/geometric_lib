'''
area(a: float, h: float): float
this function calculates area of triangle by it's side (a) and
height (h), lowered to this side
'''
def area(a, h):
    if not (isinstance(a, float) or isinstance(a, int)) or not\
           (isinstance(h, float) or isinstance(h, int)):
        raise TypeError("ERROR: incorrect arguments passed")
    if a < 0:
        raise ValueError("ERROR: triangle side can't be negative!")
    if h < 0:
        raise ValueError("ERROR: triangle height can't be negative!")
    return a * h / 2

'''
perimeter(a: float, b: float, c: float): float
this function calculates perimeter of triangle by it's three sides
'''
def perimeter(a, b, c):
    if not (isinstance(a, float) or isinstance(a, int)) or not\
           (isinstance(b, float) or isinstance(b, int)) or not\
           (isinstance(c, float) or isinstance(c, int)):
        raise TypeError("ERROR: incorrect arguments passed")
    if a < 0 or b < 0 or c < 0:
        raise ValueError("ERROR: triangle sides can't be negative!")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("ERROR: triangle with such sides doesn't exist!")
    return a + b + c
