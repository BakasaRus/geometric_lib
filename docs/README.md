# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Functions
| Function   |      Description    |
|:----------|:-------------|
| ```circle.area(int r) -> float``` | Calculating area of circle |
| ```circle.perimeter(int r) -> float``` | Calculating perimeter of circle |
| ```triangle.area(int a, int h) -> float``` | Calculating area of triangle |
| ```triangle.perimeter(int a, int b, int c) -> float``` | Calculating perimeter of triangle |
| ```square.area(int a) -> int``` | Calculating area of square |
| ```square.perimeter(int a) -> float``` | Calculating perimeter of square |
| ```square.test_func()``` | Test function |
| ```rectangle.area(int a, int b) -> float``` | Calculating area of rectangle |
| ```rectangle.perimeter(int a, int b) -> float``` | Calculating perimeter of rectangle |


# Examples
- Calculate area of rectangle:
```python
import rectangle

print("Area of rectangle with sides 2 and 5 is", rectangle.area(2, 5))
```
- Calculate area of square:
```python
import square

print("Area of square with side 7 is", square.area(7))
```
- Calculate area of circle:
```python
import circle

print("Area of circle with radius 4 is", circle.area(4))
```
- Calculate area of triangle:
```python
import triangle

print("Area of triangle with side 4 and height 7 is", triangle.area(4, 7))
```
- Calculate perimeter of circle:
```python
import circle

print("Perimeter of circle with radius 4 is", circle.perimeter(4))
```
- Calculate perimeter of triangle:
```python
import triangle

print("Perimeter of triangle with sides 3, 4 and 5 is", triangle.perimeter(3, 4, 5))
```
- Calculate perimeter of rectangle:
```python
import rectangle

print("Perimeter of rectangle with sides 4 and 5 is", rectangle.perimeter(4, 5))
```
- Calculate perimeter of square:
```python
import square

print("Perimeter of square with sides 4 is", square.perimeter(4))
```

# Commit history
```
3dbd615 (HEAD -> main) docs: add docstrings
5f2ab68 (origin/main) add: test_func
a00365b fix: perimeter function in rectangle.py
625f74b feat: add triangle.py
ce061fd feat: add rectangle.py
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
```