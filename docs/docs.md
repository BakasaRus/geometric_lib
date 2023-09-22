# Documentation
## Functionality
Allows you to calculate the area and perimeter of primitive geometric shapes (circle, rectangle, square and triangle at the moment).

## Functions
- `circle.py`
  - `def area(r)`  
    Calculates the area of a circle given its radius.
    ```
    area(1)
    #3.141592653589793
    area(5)
    #78.53981633974483  
    ``` 
  - `def perimeter(r)`  
    Calculates the perimeter of a circle given its radius.
    ```
    perimeter(1)
    #6.283185307179586
    perimeter(5)
    #31.41592653589793
    ```
- `rectangle.py`
  - `def area(a, b)`  
    Calculates the area of a rectangle given its sides lengths.
    ```
    area(1, 2)
    #2
    area(5, 7)
    #35
    ```
  - `def perimeter(a, b)`  
    Calculates the perimeter of a rectangle given its sides lengths.
    ```
    perimeter(1, 2)
    #6
    perimeter(5, 7)
    #24
    ```
- `square.py`
  - `def area(a)`
    Calculates the area of a square given its sides lengths.  
    ```
    area(1)
    #1
    area(5)
    #25
    ```
  - `def perimeter(a)`  
    Calculates the perimeter of a square given its sides lengths.
    ```
    perimeter(1)
    #4
    perimeter(5)
    #20
    ```
- `triangle.py`
  - `def area(a, h)`  
    Calculates the area of a triangle given the length of its side and height to the side.
    ```
    area(1, 1)
    #0.5
    area(10, 5)
    #25
    ```
  - `def area(a, b, c)`  
    Calculates the perimeter of a triangle given the lengths of its sides.
    ```
    perimeter(1, 1, 1)
    #3
    perimeter(3, 4, 5)
    #12
    ```