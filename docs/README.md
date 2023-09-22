# geometric_lib
**geometric_lib** contains various useful functions for calculating geometric shapes.

## Features
**geometric_lib** allows you to work with the following geometric shapes
- [Circle](https://github.com/f4ke-n0name/geometric_lib#circle)
- [Rectangle](https://github.com/f4ke-n0name/geometric_lib#rectangle)
- [Square](https://github.com/f4ke-n0name/geometric_lib#square)
- [Triangle](https://github.com/f4ke-n0name/geometric_lib#triangle)

### Circle
[Code](https://github.com/f4ke-n0name/geometric_lib/blob/main/circle.py)
```python
import math


def area(r):
	'Calculates the area of circle'
    return math.pi * r * r

```
Input: 3
Output: 28.274333882308138
```python
def perimeter(r):
	'Calculates the perimeter of circle'
    return 2 * math.pi * r
```
Input: 3
Output: 18.84955592153876

### Rectangle
[Code](https://github.com/f4ke-n0name/geometric_lib/blob/main/rectangle.py)
```python
def area(a, b):
	'Calculates the area of rectangle'
    return a * b
```
Input: 3 4 
Output: 12
```python
def perimeter(a, b):
    'Calculates the perimeter of rectangle'
    return 2 * (a + b)
```
Input: 3 4
Output: 14

### Square
[Code](https://github.com/f4ke-n0name/geometric_lib/blob/main/square.py)
```python
def area(a):
    'Calculates the area of a square'
    return a * a
```
Input: 3
Output: 9
```python
def perimeter(a):
    'Calculates the perimeter of a square'
    return 4 * a
```
Input: 3
Output: 12

### Triangle
[Code](https://github.com/f4ke-n0name/geometric_lib/blob/main/triangle.py)

```python
def area(a, h):
    'Calculates the area of triangle'
    return a * h / 2
```
Input:3 4
Output: 6

```python
def perimeter(a, b, c):
    'Calculates the perimeter of triangle'
    return a + b + c
```
Input: 3 4 5
Output: 12



## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

Project change history with commit hashes:
```console
90da1b6f1e2f9d4783ea5e0c08cf2dbfef808c5e (HEAD -> main, origin/main, origin/HEAD, lab-2) updated README.md
d3aa156c5f9f8b69eb059767391324bc17452e02 added documentation for triangle.py
63fb83b670a9e99d862298443fa19dd347a54999 added documentation for square.py
dc69d3e8d55a94249735e4e8f7963f56d7fd5fa0 added documentation for rectangle.py
5e071d9059e49f7ec28b7a5abc34c9d4901ac307 added documentation for circle.py
ac2c59492ed2c9cc47da1d5e3e113044490e7696 (origin/main, origin/HEAD, main) fixed function perimeter in rectangle.py
261ec431856661844ed8c5b76f343092e21af5ce add triangle.py
e5bae36e3a18b3b9b77867575df9b3cc9894f619 add rectangle.py
d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
```
