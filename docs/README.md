# Math formulas

**Current project provides user to calculate an area and
perimeter of circle, triangle, rectangle. square.**

## Structure of project

* `circle.py` counts area and perimetr of circle
* `rectangle.py` counts area and perimetr of rectangle
* `square.py` counts area and perimetr of square
* `triangle.py` counts area and perimetr of triangle

## Area

- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a * h / 2

## Perimeter

- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Circle functions

- Square: `area(r)` \
  \- Takes the radius of a circle, returns the area of ​​the circle of the given radius \
  _Example:_

```
from circle import area

>>> print(area(3))
9π
```

- Perimeter: `perimeter(r)` \
  \- Takes the radius of a circle, returns the perimeter of ​​the circle of the given radius \
  _Example:_

```
from circle import perimeter

>>> print(perimeter(3))
6π
```

## Rectangle functions

- Square: `area(a, b)` \
  \- Takes the width and length of a rectangle, returns the area of ​​the corresponding rectangle \
  _Example:_

```
from rectangle import area

>>> print(area(3, 5))
15
```

- Perimeter: `perimeter(a, b)` \
  \- Takes the width and length of a rectangle, returns the perimeter of ​​the corresponding rectangle \
  _Example:_

```
from rectangle import perimeter

>>> print(perimeter(3, 5)) 
16
```

## Square functions

- Square: `area(a)` \
  \- Takes the side length of a square, returns the area of ​​the corresponding square \
  _Example:_ 

```
from square import area

>>> print(area(3))
9
```

- Perimeter: `perimeter(a)` \
  \- Takes the side length of a square, returns the perimeter of ​​the corresponding square \
  _Example:_ 

```
from square import perimeter

>>> print(perimeter(3))
12
```

## Triangle functions

- Square: `area(a, h)` \
  \- Takes the side length and height of a triangle, returns the area of ​​the corresponding triangle \
  _Example:_

```
from triangle import area

>>> print(area(3, 4)) 
6
```

- Perimetr: `perimeter(r)` \
  \- Takes the side length and height of a triangle, returns the perimeter of ​​the corresponding triangle \
  _Example:_

```
from triangle import perimeter

>>> print(perimeter(3, 4, 5))
12
```

## Git commit history

| Hash commit | Message                                                   |
|-------------|-----------------------------------------------------------| 
| 9d0e2dd     | (HEAD -> lab2_408847, origin/lab2_408847) add git history | 
| 2fd31d1     | remove pdf instruction                                    |
| 30002b5     | refactor readme                                           | 
| 30a3b98     | refactor readme                                           | 
| fe1b456     | refactor readme                                           | 
| 968a3e6     | refactor readme                                           |                                        
| a36c169     | refactor readme                                           |                                         
| c90c49d     | refactor readme                                           |                                           
| 0bd3695     | commented functions                                       |

> Made by Engozdev. Contacts: <denacua5@gmail.com> 
