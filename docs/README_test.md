# Documentation for *unittest*

## Testing goals and objectives

### Goals of testing: 
Check the correct operation of the functions for calculating **area** and **perimeter** of 
geometric figures implemented in the circle, rectangle, square, triangle modules. 

### Objectives of testing:
Implement testing functions based on *unittest* for the functions for calculating 
**area** and **perimeter** of geometric figures implemented in the circle, rectangle, square, triangle modules.

## Description of tested product

### **Circle**

#### *Main functions*

* `def area(r)`
```
Returns the area of a circle

Options:
    r (int/float): circle radius value

Return value:
    math.pi * r * r (int/float): area of a circle
```

* `def perimeter(r)`
```
Returns the perimeter of a circle

Options:
    r (int/float): circle radius value

Return value:
    math.pi * r * r (int/float): perimeter of a circle
```
####
#### [*Examples*](https://github.com/ElizarAlexey777/geometric_lib#circle)
####

### **Rectangle**

#### *Main functions*

* `def area(a, b)`
```
Returns the area of a rectangle

Options:
    a (int/float): size of the side of the rectangle (first side) \n
    b (int/float): size of the side of the rectangle (adjacent to the first side)

Return value:
    a * b (int/float): area of the rectangle
```

* `def perimeter(a, b)`
```
Returns the perimeter of a rectangle

Options:
    a (int/float): size of the side of the rectangle (first side) \n
    b (int/float): size of the side of the rectangle (adjacent to the first side)

Return value:
    (a + b) * 2 (int/float):perimeter of a rectangle
```

####
#### [*Examples*](https://github.com/ElizarAlexey777/geometric_lib#rectangle)
####

### **Square**

#### *Main functions*

* `def area(a)`
```
Returns the area of a square

Options:
    a (int/float): square side size

Return value:
    a * a (int/float): square area size
```

* `def perimeter(a)`
```
Returns the perimeter of a square

Options:
    a (int/float): square side size

Return value:
    4 * a (int/float): square perimeter size
```

####
#### [*Examples*](https://github.com/ElizarAlexey777/geometric_lib#square)
####

### **Triangle**

#### *Main functions*

* `def area(a, h)`
```
Returns the area of a triangle

Options:
    a (int/float): size of the side of the triangle to which the height is build \n
    h (int/float): height of triangle

Return value:
    a * h / 2 (int/float): area of the triangle
```

* `def perimeter(a, b, c)`
```
Returns the perimeter of a triangle

Options:
    a (int/float): size of the first side of the triangle
    b (int/float): size of the second side of the triangle
    c (int/float): size of the third side of the triangle

Return value:
    a + b + c (int/float): perimeter of the triangle
```

####
#### [*Examples*](https://github.com/ElizarAlexey777/geometric_lib#triangle)
####

## Test area

### Testing will have the following aspects:

1) Correct calculation of area and perimeter for various sizes.
2) Processing of zero and negative values of input parameters.
3) Testing on very large numbers.

## Testing Strategies

#### Use a combined approach, including unit testing of each module separately (functional testing)
For each module, tests will be carried out to ensure the correctness of the calculations, 
error handling and compliance of the results with the expected values

## Result

|       Module        | Number of tests passed |   Number of failed tests    |                                                                                                                     
|:-------------------:|:----------------------:|:---------------------------:|
|     circle.area     |           3            |              1              |                                                                                   
|  circle.perimeter   |           3            |              1              |                                                                                       
|   rectangle.area    |           3            |              1              | 
| rectangle.perimeter |           2            |              2              | 
|     square.area     |           3            |              1              |                                                                        
|  square.perimeter   |           3            |              1              |                                                                                
|    triangle.area    |           3            |              1              | 
| triangle.perimeter  |           2            |              2              | 

> Total tests: 32  
> 22 tests completed ✅  
> 10 tests failed ❌

## Сonclusion

> The main testing goals were achieved.   
> Failed tests have been identified due to the fact that we incorrectly 
calculate area and perimeter for negative and zero values.