# Contents

- [Math formulas](#math-formulas)
  - [Area](#area)
  - [Perimeter](#perimeter)
- [Rectangle](#rectangle)
- [Circle](#circle)
- [Triangle](#triangle)
- [Square](#square)

# Math formulas

## Area

- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## Perimeter

- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: S = a + b + c



# Rectangle

## Functions

### area(a, b)

   - call example: 

```python
from rectangle import area
rec_area = area(10, 20)
print(rec_area) # 200
```    

   - params
     - a - first side of rectangle 
     - b - second side of rectangle
   - returns
     - a * b - area of rectangle

### perimeter(a, b)

  - call example: 

```python
from rectangle import perimeter
rec_perimeter = perimeter(5, 10)
print(rec_perimeter) # 30
```    

   - params
     - a - first side of rectangle 
     - b - second side of rectangle
   - returns
     - (a + b) * 2 - perimeter of rectangle


# Circle

## Functions

### area(r)

  - call example: 

```python
from circle import area
c_area = area(10)
print(c_area) # 314.1592653589793
```    

   - params
     - r - radius of circle 
   - returns
     - pi * r * r - area of circle

### perimeter(a, b)

  - call example: 

```python
from circle import perimeter
c_perimeter = perimeter(10)
print(c_perimeter) # 62.83185307179586
```

   - params
     - r - radius of circle 
   - returns
     - 2 * pi * r - perimeter of circle


# Triangle

## Functions

### area(a, h)

  - call example: 

```python
from triangle import area
tr_area = area(10, 20)
print(tr_area) # 100
```    

   - params
     - a - base of triangle 
     - h - height of triangle 
   - returns
     - a * h / 2 - area of triangle

### perimeter(a, b, c)

  - call example: 

```python
from triangle import perimeter
tr_perimeter = perimeter(5, 10, 12)
print(tr_perimeter) # 27
```  

   - params
     - a - first side of triangle 
     - b - second side of triangle
     - c - third side of triangle
   - returns
     - a + b + c - perimeter of triangle

# Square

## Functions

### area(a)
  - call example: 

```python
from square import area
sq_area = area(10)
print(sq_area) # 100
```    

   - params
     - a - side of square 
   - returns
     - a * a - area of square

### perimeter(a, b, c)

  - call example: 

```python
from square import perimeter
sq_perimeter = perimeter(5)
print(sq_perimeter) # 20
```  

   - params
     - a - side of square 
   - returns
     - a * 4 - perimeter of square

## Modification history

- _13ea531_ __docs__: Add doc string for testing classes/modules
- _6704671_ __feat__: Add package test
- _62cf568_ __feat__: Add tests modules
- _0b1f9af_ __docs__: Add docstring for functions in triangle.py
- _7e6c02b_ __docs__: Add docstring for functions in square.py
- _fbb1a17_ __docs__: Add docstring for functions in rectangle.py
- _fff07ba_ __docs__: Add docstrings for functions in circle.py
- _1de3ebb_ __fix__: Fixed perimetr function
- _9737c19_ __feat__: Add new file triangle.py
- _7b7c91c_ __feat__: Add new file rectangle.py
- _d078c8d_ __L-03__: Docs added
- _8ba9aeb_ __L-03__: Circle and square added
