# Documentation for unittest

## Testing goals and objectives

### Goals of testing: 
Check the correct operation of the functions for calculating **area** and **perimeter** of 
geometric figures implemented in the circle, rectangle, square, triangle modules. 

### Objectives of testing:
Implement testing functions based on unittest for the functions for calculating 
*area* and *perimeter* of geometric figures implemented in the circle, rectangle, square, triangle modules.

## Description of tested product

### **Circle**

#### *Main functions*

* `def area(r)`
```
Returns the area of a circle
Options:
    r (int/float)
Return value:
    math.pi * r * r (float)
```

* `def perimeter(r)`
```
Returns the perimeter of a circle
Options:
    r (int/float)
Return value:
    math.pi * r * r (float)
```

### **Rectangle**

#### *Main functions*

* `def area(a, b)`
```
Returns the area of a rectangle
Options:
    a (int/float)
    b (int/float)
Return value:
    a * b (int/float)
```

* `def perimeter(a, b)`
```
Returns the perimeter of a rectangle
Options:
    a (int/float)
    b (int/float)
Return value:
    (a + b) * 2 (int/float)
```



### **Square**

#### *Main functions*

* `def area(a)`
```
Returns the area of a square
Options:
    a (int/float)
Return value:
    a * a (int/float)
```

* `def perimeter(a)`
```
Returns the perimeter of a square
Options:
    a (int/float)
Return value:
    4 * a (int/float)
```



### **Triangle**

#### *Main functions*

* `def area(a, h)`
```
Returns the area of a triangle
Options:
    a (int/float)
    h (int/float)
Return value:
    a * h / 2 (int/float)
```

* `def perimeter(a, b, c)`
```
Returns the perimeter of a triangle
Options:
    a (int/float)
    b (int/float)
    c (int/float)
Return value:
    a + b + c (int/float)
```


## Test area

### Testing will have the following aspects:

1) Processing of zero and negative values of input parameters.
2) Correct calculation of area and perimeter for various sizes.
3) Testing on large numbers.

## Testing Strategies

#### Use a combined approach, including unit testing of each module separately (functional testing)
For each module, tests will be carried out to ensure the correctness of the calculations, 
error handling and compliance of the results with the expected values

## Result

|       Module        | Number of tests passed | Number of failed tests |                                                                                                                     
|:-------------------:|:----------------------:|:----------------------:|
|     circle.area     |           3            |           1            |                                                                                   
|  circle.perimeter   |           3            |           1            |                                                                                       
|   rectangle.area    |           3            |           2            | 
| rectangle.perimeter |           2            |           2            | 
|     square.area     |           3            |           1            |                                                                        
|  square.perimeter   |           2            |           1            |                                                                                
|    triangle.area    |           3            |           2            | 
| triangle.perimeter  |           2            |           2            | 

> Total tests: 34  
> 21 tests completed ✅  
> 13 tests failed ❌
## Сonclusion

> The main testing goals were achieved.   
> Failed tests have been identified due to the fact that we incorrectly 
calculate area and perimeter for negative and zero values.