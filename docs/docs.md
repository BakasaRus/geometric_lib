# Documentation
## Functionality
Allows you to calculate the area and perimeter of primitive geometric shapes (circle, rectangle, square and triangle at the moment).

## Functions
- `circle.py`
  - `def area(r)`  
    Calculates the area of a circle given its radius.
    ```py
    import circle
    
    print(circle.area(1))
    #3.141592653589793
    print(circle.area(5))
    #78.53981633974483  
    ``` 
  - `def perimeter(r)`  
    Calculates the perimeter of a circle given its radius.
    ```py
    import circle
    
    print(circle.perimeter(1))
    #6.283185307179586
    print(circle.perimeter(5))
    #31.41592653589793
    ```
- `rectangle.py`
  - `def area(a, b)`  
    Calculates the area of a rectangle given its sides lengths.
    ```py
    import rectangle
    
    print(rectangle.area(1, 2))
    #2
    print(rectangle.area(5, 7))
    #35
    ```
  - `def perimeter(a, b)`  
    Calculates the perimeter of a rectangle given its sides lengths.
    ```py
    import rectangle
    
    print(rectangle.perimeter(1, 2))
    #6
    print(rectangle.perimeter(5, 7))
    #24
    ```
- `square.py`
  - `def area(a)`
    Calculates the area of a square given its sides lengths.  
    ```py
    import square
    
    print(square.area(1))
    #1
    print(square.area(5))
    #25
    ```
  - `def perimeter(a)`  
    Calculates the perimeter of a square given its sides lengths.
    ```py
    import square
    
    print(square.perimeter(1))
    #4
    print(square.perimeter(5))
    #20
    ```
- `triangle.py`
  - `def area(a, h)`  
    Calculates the area of a triangle given the length of its side and height to the side.
    ```py
    import triangle
    
    print(triangle.area(1, 1))
    #0.5
    print(triangle.area(10, 5))
    #25
    ```
  - `def area(a, b, c)`  
    Calculates the perimeter of a triangle given the lengths of its sides.
    ```py
    import triangle
    
    print(triangle.perimeter(1, 1, 1))
    #3
    print(triangle.perimeter(3, 4, 5))
    #12
    ```

## Commit history (from old to new)
1. `commit 8ba9aeb3cea847b63a91ac378a2a6db758682460`  
  Adds circle and square.
2. `commit d078c8d9ee6155f3cb0e577d28d337b791de28e2`  
  Adds docs.
3. `commit 25a1142ee881b4a33824b67c0f42dc9174c4b49b`  
  Adds rectangle.
4. `commit 386f7bd288c265e218cac2745d04059c6d1cb882`  
  Fixes wrong rectangle perimeter calculation.
5. `commit d392c50fee00acddd05a6f6395b320970814508c`  
  Adds docstrings to all functions of circle, rectangle, square, triangle.
6. `commit 9911095736925cd3cc21a01e52350067c79adc05`  
  Adds docs/docs.md - file that contains all documentation for project.