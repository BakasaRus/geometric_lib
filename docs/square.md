# square.py

## square.area()
```python
square.area(a: Union[int, float]) -> Union[int, float]
```
Принимает длину стороны квадрата и возвращает площадь квадрата
#### Параметры:
* **a** (int или float) - сторона квадрата

#### Возвращает:
* (int или float) - площадь квадрата со стороной a

#### Пример:

```python
from geometric_lib import square

side = 3
print(square.area(side))
```



## square.perimeter()
```python
square.perimeter(a: Union[int, float]) -> Union[int, float]
```
Принимает длину стороны квадрата и возвращает периметр квадрата
#### Параметры:
* **a** (int или float) - сторона квадрата

#### Возвращает:
* (int или float) - периметр квадрата со стороной a

#### Пример:

```python
from geometric_lib import square

side = 5
print(square.perimeter(side))
```


