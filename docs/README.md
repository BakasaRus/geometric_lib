# Geometric Lib

## Math formulas

### Area


- Circle: $S = \pi R^2$
- Rectangle: $S = ab$
- Square: $S = a^2$
- Triangle: $S = \frac{1}{2} ah$

### Perimeter

- Circle: $P = 2\pi R$
- Rectangle: $P = 2a + 2b$
- Square: $P = 4a$
- Triangle: $P = a + b + c$

## Function descriptions

### Circle functions

- area(r)

  Takes the radius of the circle, returns area of the circle

```
>>> print(area(2)) 
12.566370614359172
```

- perimeter(r)

  Takes the radius of the circle, returns perimeter of the circle

```
>>> perimeter(1)
6.283185307179586
```

### Rectangle functions

- area(a, b)

  Takes the lengths of the two sides of rectangle, returns area of the rectangle

```
>>> area(2, 3)
6
```

- perimeter(a, b)

  Takes the lenghts of the two sides of rectangle, returns perimeter of the rectangle

```
>>> perimeter(2, 3) 
10
```

### Square functions

- area(a)

  Takes the length of the side of square, returns area of the square

```
>>> area(2) 
4
```

- perimeter(a)

  Takes the lenght of the side of square, returns perimeter of the square

```
>>> perimeter(3)
12
```

### Triangle functions

- area(a, h)
  Takes the length of the side of triangle and the lenght of height, returns area of the triangle

```
>>> area(2, 3)
3
```

- perimeter(a, b, c)
  Takes the lenghts of the three sides of triangle, returns perimeter of the triangle

```
>>> perimeter(3, 4, 5)
12
```

## Git commit history

| Hash     | Message                                                                    |
|:---------|:---------------------------------------------------------------------------|
| 514234b  | (HEAD -> lab2_409093, origin/lab2_409093) docs: correction of innaccuracy  |
| 49138a1  | docs: add git commit history                                               |
| 26a4766  | docs: update docs catalog                                                  |
| 495e6b7  | docs: add comments to the functions                                        |
| 7773f59  | (origin/main, origin/HEAD, main) fix: fix a perimeter calculation error    |
| ef4f9ff  | feat: add rectangle.py file                                                |
| d078c8d  | L-03: Docs added                                                           |
| 8ba9aeb  | L-03: Circle and square added                                              |

