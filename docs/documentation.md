# Documentation

 ## General description of the project

 Geometric_lib is a project designed to work with geometric shapes and operations on them. With its help, you can calculate the area and perimeter of various geometric shapes (circle, rectangle, square and triangle).

 ## Description of modules
 
 - ### circle.py 
  
    - #### Functions

        `def area(r)` takes the value of radius r and returns the area of a circle with radius r.  
        `def perimeter(r)` takes the value of radius r and returns the perimeter of a circle with radius r.

    - #### Output examples

        `area(3)` returns 28.274333882308138  
        `perimeter(3)` returns 18.84955592153876 

 - ### reactangle.py
   
    - #### Functions

        `def area(a, b)` takes the value of sides a, b and returns the area of a rectangle with sides a, b.  
        `def perimeter(a, b)` takes the value of sides a, b and returns the perimeter of a rectangle with sides a, b.

    - #### Output examples

        `area(3, 4)` returns 12  
        `perimeter(3, 4)` returns 14 

 - ### square.py
   
    - #### Functions

        `def area(a)` takes the value of side a and returns the area of a square with side a.  
        `def perimeter(a)` takes the value of side a and returns the perimeter of a square with side a.

    - #### Output examples

        `area(3)` returns 9  
        `perimeter(3)` returns 12 

 - ### triangle.py
   
    - #### Functions

        `def area(a, h)` takes the value of side a and height h and returns the area of a triangle with side a and height h.  
        `def perimeter(a, b, c)` takes the value of sides a, b, c and returns the perimeter of a triangle with sides a, b, c.

    - #### Output examples

        `area(2, 3)` returns 3  
        `perimeter(3, 7, 4)` returns 14 

 - ## tests

    Module for testing functions from the geometric-lib  
   
    - ### test_circle.py

        Tests functions for calculating area and perimeter for circle with zero, small and big data            

    - ### test_rectangle.py

        Tests functions for calculating area and perimeter for rectangle with zero, small and big data  

    - ### test_square.py

        Tests functions for calculating area and perimeter for square with zero, small and big data            

    - ### test_triangle.py

        Tests functions for calculating area and perimeter for triangle with zero, small and big data  

     
## Commit history

1. commit `8ba9aeb3cea847b63a91ac378a2a6db758682460`  
L-03: Circle and square added
2. commit `d078c8d9ee6155f3cb0e577d28d337b791de28e2`  
L-03: Docs added
3. commit `c5ec6fc4412b2c02cbd935f073b2e1bb8d10bf09`  
added file rectangle.py
4. commit `62e2072ab3521f9f3842f7aace185fe7da2fbd25`  
fixed bug in rectangle.py and added triangle.py
5. commit `05b924400ca8f9352b91bbc5d12451e0e59d7df9`  
added description of functions in circle.py, rectangle.py, square.py, triangle.py
6. commit `d7b558de7f55acaf079a77c3fb68a9a76d39576e`  
 added file documentation.md with documentation of project
7. commit `10bfd9adc2eb40523cf9fc5b118208971be3759b`  
update documentation.md
7. commit `7d627a438c5db731c56611f2802f602026e5e476`  
added module tests with test_rectangle.py, test_triangle.py, test_circle.py, test_square.py
8. commit `a2a5227a130912d9e0d7f691d33be8f1f12c683f`  
updated documentation.md
9. commit `bcaa66fe0118a5f781dfb381ee4611bbb6bd8df6`  
added new tests for modules