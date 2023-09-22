# Math calculations
This project contains Python scripts, which can calculate area and perimeter of some shapes. Currently supported shapes are: circle, rectangle, square, triangle. For circle perimeter is circumference length. Calculations are performed by the following formulas:

## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2(a+b)
- Square: P = 4a
- Triangle: abc

For every shape there is *SHAPE*.py file, which contains `area` and `perimeter` functions. They're always receive real number argument(s) and return real number result

## Examples
```
# calculate circle area
import circle
circle.area(1) # 1 is radius, result is 3.1415926...

# calculate rectangle perimeter
import rectangle
rectangle.perimeter(2, 3) # 2, 3 are lengths of rectangle sides, result is 12

# calculate triangle area
import triangle
triangle.area(4, 2.2) # 4 is side length, 2.2 is height lowered to this side, result is 4.4
```
Descriptions of all functions for each shape can be found in *SHAPE*.py files in comments
