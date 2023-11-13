# triangle.py

## triangle.area()
```python
triangle.area(a: Union[int, float], h: Union[int, float]) -> Union[int, float]
```
Принимает длину основания и высоту, перпендикулярную основанию, треугольника и
    возвращает площадь треугольника
#### Параметры:
* **a** (int или float) - сторона треугольника
* **h** (int или float) - высота треугольника


#### Возвращает:
* (int или float) - площадь треугольника

#### Пример:

```python
from geometric_lib import triangle

a = 3
b = 4
c = 5
h = 4
print(triangle.area(a, h))
```



## triangle.perimeter()
```python
triangle.perimeter(
    a: Union[int, float], 
    b: Union[int, float], 
    c: Union[int, float]
) -> Union[int, float]
```
Принимает длину сторон треугольника и возвращает периметр треугольника
#### Параметры:
* **a** (int или float) - 1-ая сторона треугольника
* **b** (int или float) - 2-ая сторона треугольника
* **c** (int или float) - 3-ая сторона треугольника

#### Возвращает:
* (int или float) - периметр треугольника

#### Пример:

```python
from geometric_lib import triangle

a = 3
b = 4
c = 5
h = 4
print(triangle.perimeter(a, b, c))
```


