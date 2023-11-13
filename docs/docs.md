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
| Hash    | Author     | Time                           | Message                                                                  |
|---------|------------|--------------------------------|--------------------------------------------------------------------------|
| 8ba9aeb | rinnothing | Fri Sep 22 11:59:50 2023 +0300 | Adds circle and square.                                                  |
| d078c8d | rinnothing | Fri Sep 22 10:34:21 2023 +0300 | Adds docs.                                                               |
| 25a1142 | rinnothing | Mon Sep 4 15:38:19 2023 +0300  | Adds rectangle.                                                          |
| 386f7bd | rinnothing | Mon Sep 4 15:30:37 2023 +0300  | Fixes wrong rectangle perimeter calculation.                             |
| d392c50 | rinnothing | Thu Mar 4 14:55:29 2021 +0300  | Adds docstrings to all functions of circle, rectangle, square, triangle. |
| 9911095 | rinnothing | Thu Mar 4 14:54:08 2021 +0300  | Adds docs/docs.md - file that contains all documentation for project.    |
| ded52ed | rinnothing | Thu Nov 2 10:44:56 2023 +0300  | Adds tests/testing_plan.md - testing plan.                               |
| f162ada | rinnothing | Thu Nov 2 11:45:05 2023 +0300  | Adds unittests                                                           |
| 9b81bd0 | rinnothing | Mon Nov 13 12:57:31 2023 +0300 | tests: add tests for wrong arguments (now they break program)            |
| cc6d436 | rinnothing | Mon Nov 13 13:10:52 2023 +0300 | tests: make tests checking errors                                        |
| 74bcac5 | rinnothing | Mon Nov 13 13:24:33 2023 +0300 | tests: remove pytest add unittest                                        |