# Geometric lib
Library uses functions providing several geometric formulas.
1. [Area](#area)
2. [Perimeter](#perimeter)
3. [Function description](#functions-description)
    
    -[circle.py](#circlepy)

    -[rectangle.py](#rectanglepy)

    -[square.py](#squarepy)

    -[triangle.py](#trianglepy)

4. [Commit history](#commit-history)
## Area
- Circle: $S = \pi R^2$
- Rectangle: $S = ab$
- Square: $S = a^2$

## Perimeter
- Circle: $P = 2πR$
- Rectangle: $P = 2a + 2b$
- Square: $P = 4a$

## Functions description
### circle.py
- area

   Takes <b>r</b> - radius, returns area
   
   ```python
   print(area(3))
   ```
- perimeter

   Takes <b>r</b>  - radius, returns perimeter of the circle

   ```python
   print(perimiter(3))
   ```
### rectangle.py
- area

  Takes <b>a, b</b>- length of sides of the rect, returns area

  ```python
  print(area(3, 4))
  ```

- perimeter

    Takes <b>a, b</b>- length of sides of the rect, returns perimeter

    ```python
    print(perimter(3, 4))
    ```

### square.py

- area
    
    Takes <b>a</b> - side, returns area
   
   ```python
   print(area(3))
   ```
- perimeter

   Takes <b>a</b>  - side, returns perimeter of the square

   ```python
   print(perimeter(3))
   ```

### triangle.py

- area
    
    Takes <b>a, h</b> - side and height of the triangle, returns area

    ```python
    print(area(2, 4))
    ```

- perimeter

    Takes <b>a, b, c</b> - sides of the triangle, returns perimeter

    ```python 
    print(perimeter(4, 4, 4))
    ```

## Commit history
| Hash     | Branch    |Message   |
| ---------|-----------|----------|
|717f0dc|lab2|add in README.md v2|
|2ebf664   |lab2     |add image with commits|
|43821c2   |lab2     |add function description|
|6572d73   |docs       |add in Readme|
|e72285d   |main       |add Readme.md|
|3c768bf   |main       |func description|

