# **_Geometric Lib_**
## General description of the project
> Geometric Lib is a project designed to work with various geometric shapes on a plane. For example, it can be used to calculate the area and perimeter of such shapes as a circle, triangle, square and rectangle.

## Description of functions
- ## _Circle_
    - ### Function
        - `def area(r)` The function takes the value **_r_** and returns the area of a circle with this radius.

        - `def perimeter(r)` The function takes the value **_r_** and returns the length of a circle of this radius.

    - ### Examples
        - Call `area(4)` returns _50.26548245743669_
        - Call `perimeter(4)` returns _25.132741228718345_
- ## _Rectangle_
    - ### Function
        - `def area(a, b)` The function takes the values **_a_** and **_b_** and returns the area of a rectangle with this heigh and width.

        - `def perimeter(r)` The function takes the values **_a_** and **_b_** and returns the perimeter of a rectangle with this heigh and width.
    - ### Examples
        - Call `area(4.51, 12)` returns _54.12_
        - Call `perimeter(4.51, 12)` returns _33.019999999999996_
- ## _Square_
    - ### Function
        - `def area(a)` The function takes the value **_a_** returns the area of a square with such a side.

        - `def perimeter(a)` The function takes the value **_a_** returns the perimeter of a square with such a side.
    - ### Examples
        - Call `area(412)` returns _169744_
        - Call `perimeter(412)` returns _1648_

- ## _Triangle_
    - ### Function
        - `def area(a, h)` The function takes the values **_a_** and **_h_** returns the area of a triangle with this side and the height lowered to this side.

        - `def perimeter(a, b, c)` The function takes the values **_a_**, **_b_** and **_c_** returns the perimeter of a triangle with such sides.
    - ### Examples
        - Call `area(4, 3)` returns _6.0_
        - Call `perimeter(3, 4, 5)` returns _12_

## Project modification history
1. Commit hash: `8ba9aeb3cea847b63a91ac378a2a6db758682460`
    - L-03: Circle and square added
2. Commit hash: `d078c8d9ee6155f3cb0e577d28d337b791de28e2`
    - L-03: Docs added
3. Commit hash: `4d04f975f77a794ca8d54bcec8b6c6c93908c9fb`
    - Added rectangle.py
4. Commit hash: `c7998c83a2bec2472c5b80ddd4889b99a99134fe`
    - Fixed a bug in rectangle.py
5. Commit hash: `ffc224485d03b6950fb56a9a562ff9664376309d `
    - Add file documentation triangle.py, square.py, rectangle.py, circle.py


