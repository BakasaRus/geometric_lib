# Geometric_Lib

**Geometric_Lib** provides utility functions for the computation the 
properties of geometric shapes. 

## Features
**Geometric_Lib** provides the ability to work with the following geometric 
shapes:
- [Circle](https://github.com/ElizarAlexey777/geometric_lib#circle)
- [Rectangle](https://github.com/ElizarAlexey777/geometric_lib#rectangle)
- [Square](https://github.com/ElizarAlexey777/geometric_lib#square)
- [Triangle](https://github.com/ElizarAlexey777/geometric_lib#triangle)

### Circle
Link to current [code](https://github.com/ElizarAlexey777/geometric_lib/blob/main/circle.py)
```python
import math 

def area(r): # Returns the area of a circle
    return math.pi * r * r

Input: 4
Output: 50.26548245743669
```
```python
import math

def perimeter(r): # Returns the perimeter of a circle
    return 2 * math.pi * r

Input: 4
Output: 25.132741228718345
```
### Rectangle
Link to current [code](https://github.com/ElizarAlexey777/geometric_lib/blob/main/rectangle.py)
```python
def area(a, b): # Returns the area of a rectangle
    return a * b

Input: 4 8
Output: 32
```
```python
def perimeter(a, b): # Returns the perimeter of a rectangle
    return (a + b) * 2

Input: 4 8
Output: 24
```
### Square
Link to current [code](https://github.com/ElizarAlexey777/geometric_lib/blob/main/square.py)
```python
def area(a): # Returns the area of a square
    return a * a

Input: 4
Output: 16
```
```python
def perimeter(a): # Returns the perimeter of a square
    return 4 * a

Input: 5
Output: 20
```
### Triangle
Link to current [code](https://github.com/ElizarAlexey777/geometric_lib/blob/main/triangle.py)
```python
def area(a, h): # Returns the area of a triangle
    return a * h / 2

Input: 4 8
Output: 16
```
```python
def perimeter(a, b, c): # Returns the perimeter of a triangle
    return a + b + c

Input: 3 4 5
Output: 12
```


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

## Project history
> Project creation date: 06/09/2023  
> Last commit: 21/09/2023

Project change history with commit hashes:
```console
7953ef05e2881d2efd22e41f1646090baa4dd190 (HEAD -> main, origin/main, origin/HEAD) fix: change the language of description blocks in functions, square.py: rus->eng
732880b722aee2f1dc0120dacbc7c724f0d7f72b fix: change the language of description blocks in functions, circle.py: rus->eng
8c342699e20ed7337b58131e8e247115cdd61fc2 fix: change the language of description blocks in functions, triangle.py: rus->eng
1dd4211098e1af4279e6c02ae75ef9fa333c6d79 fix: change the language of description blocks in functions: rus->eng
3ae40e4c55ba6cfd91f9c65677f23f6e8e647951 docs: upd README.md structure
47c9adabb81130b97a01d78cce27362fc06b111e docs: added description blocks for all triangle.py functions
3a45e803e7ed87df1b7cdcc024eab93ecdd1de3f docs: added description blocks for all square.py functions
d082e1e123a3e3bb61e5bc973f394e2a751b2084 docs: added description blocks for all rectangle.py functions
827725627bb692f012277e9102b4affeffbb1898 docs: added description blocks for all circle.py functions
2dcfa974063c6870382726ba7f36c713721636a6 (new_features_408582) fix: calculating the perimeter of a rectangle
75f48ec16575903b5ceb2743643d914cc30c5431 feat: add triangle.py
67e5084cd6efb479133511ec2ea9ce23360f0591 feat: add rectangle.py
d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
```


## License And QA
Code ported from [Smartiqa Org](https://github.com/smartiqaorg/geometric_lib).

@ElizarAlexey777 What do you think about these?
