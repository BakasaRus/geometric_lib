# Math formulas

## Area

- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter

- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Solution description

This module calculates area and perimeter of the following geometrig objects:
- triangle
- rectangle
- square
- circle
# Function description

## triangle.py

- `perimeter`
	Returns perimeter of triangle with sides a, b and c
```python
#Example
from triangle import perimeter

P = perimeter(2.5, 3, 16)
print(P) # out: 21.5
```
- `area`
	Returns area of triangle with side a and height h
```python
#Example
from triangle import area

S = area(2.5, 4)
print(S) # out: 5
```
## rectangle.py

- `perimeter`
	Returns perimeter of rectangle with sides a and b
```python
#Example
from rectangle import perimeter

P = perimeter(2.5, 3)
print(P) # out: 11
```
- `area`
	Returns area of rectangle with sides a and b
```python
#Example
from rectangle import area

S = area(2.5, 4)
print(S) # out: 10
```
## circle.py

- `perimeter`
	Returns perimeter of circle with radious r
```python
#Example
from circle import perimeter

P = perimeter(2.5)
print(P) # out: 15.70795...
```
- `area`
	Returns area of circle with radious r
```python
#Example
from circle import area

S = area(2.5)
print(S) # out: 24.67396...
```
## square.py

- `perimeter`
	Returns perimeter of circle with radious r
```python
#Example
from square import perimeter

P = perimeter(3)
print(P) # out: 3
```
- `area`
	Returns area of circle with radious r
```python
#Example
from square import area

S = area(3)
print(S) # out: 9
```
# Project history

- *f202900* docs: docs/README.md solution description with examples added
- *1408e96* feat: add comments
- *928f172* bag in file triagnle.py fixed
- *401415a* bag in rectangle.py fixed, new file triangle.py added
- *c7cba0c* new file rectangle.py added
- *d078c8d* L-03: Docs added
- *8ba9aeb* L-03: Circle and square added