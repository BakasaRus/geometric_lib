# Tests report

### Goals of testing

- Check the correctness of calculations
- Find out behavior of the program when input data is incorrect
- View the behavior of the program with incorrect input data

### geometric_lib overview

This library implements some math functions for working with geometry figures. Therefore it must to:

- Make correct calculations for all these functions if the input data is correct
- If the input is incorrect, the function should return an error message
- There should not be a situation when the program runs indefinitely

### Testing scope

This test report covers testing of every function in the library:

- `circle.py`
    * area
    * perimeter
- `rectangle.py`
    * area
    * perimeter
- `square.py`
    * area
    * perimeter
- `triangle.py`
    * area
    * perimeter

### Testing overview

This testing is based on unit tests. This is unit testing using the `Black box` model. Test plan:

- Correct testing
- Failure
- Speed testing

### Successful tests params

- All the tests for `correctness` have been passed
- All tests for `failure` have been passed
- Total `execution` time (including tests with a large number of tests) - less than 1 second

### Expected result

Based on the git commit log, it can be assumed that the developer of this library has noticed errors in logistics and (
possibly) has already done some manual testing.

# Result

## Testing results

- test_circle.py

```
    Ran 8 tests in 0.000s

    OK
```

- test_rectangle.py

```
    Ran 8 tests in 0.000s

    OK
```

- test_square.py

```
    Ran 8 tests in 0.000s

    OK
```

- test_triangle.py

```
    Ran 8 tests in 0.000s

    OK
```

## Сonclusion

`All tests are passed`