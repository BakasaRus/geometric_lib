# Tests report

## Goals of testing
- Check if calculations are correct
- Find out behavior of the program when input data is incorrect
- Check speed of execution

## geometric_lib overview
This library implements some math functions for working with geometry figures. Therefore it must to:
- Make correct calculations on all these functions if the input data is correct
- If the input is incorrect, function should raise error
- There should not be a situation when programm runs endlessly

## Testing scope
This tests report covers testing of every function in the library:
- circle.py
    * area
    * perimeter
- rectangle.py
    * area
    * perimeter
- square.py
    * area
    * perimeter
- triangle.py
    * area
    * perimeter

## Testing overview
This testing is based on unit tests. It is modular testing with _Black box_ model. Plan of testing:
- Сorrectness testing (positive and negative)
- Failsafety
- Speed testing

## Successful tests params
- All _correctness_ tests are passed
- All _failsafety_ tests are passed
- Whole execution time (include big numbers tests) -- less than 1 second

## Expected result
Based on log of git commits one may assume that developer of this library has noticed the bugs in the logistics and (maybe) has already done some manual testing.


## Result
# Testing results
- circle.py
```
    Ran 8 tests in 0.001s

    FAILED (failures=2)
```
- rectangle.py
```
    Ran 8 tests in 0.001s

    FAILED (failures=2)
```

- square.py
```
    Ran 8 tests in 0.001s

    FAILED (failures=2)
```

- triangle.py
```
    Ran 8 tests in 0.001s

    FAILED (failures=3)
```

# Сonclusion
Neither function checks the input data. Unreal values can be passed to it and no errors will raised. It is about second point of tests goal. Moreover _triangle.py_ _area_ function may return float when it is possible to return int (this agrees with the docs, but may not be an obvious solution)