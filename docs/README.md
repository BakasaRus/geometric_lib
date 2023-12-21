# geometric\_lib

Данная библиотека представляет собой набор функций для вычисления площадей и периметров различных геометрических фигур. Каждая фигура представлена в виде отдельного модуля, содержащего функции расчёта.

## Документация

### Круг `circle.py`

#### `area(r)`

Функция принимает радиус круга `r` и возвращает площадь круга, рассчитанную по формуле `πr²`

Пример использования:
```python
import circle

# Вычисление площади круга
area_result = circle.area(5)
print(area_result)  # Вернет 78.53...
```

#### `perimeter(r)`

Функция принимает радиус окружности `r` и возвращает длину (периметр) окружности, рассчитанный по формуле `2πr`

Пример использования:
```python
import circle

# Вычисление периметра окружности
perimeter_result = circle.perimeter(5)
print(perimeter_result)  # Вернет 31.41...
```

### Прямоугольник `rectangle.py`

#### `area(a, b)`

Функция принимает стороны прямоугольника `a` и `b` и возвращает площадь прямоугольника, рассчитанный по формуле `a * b`

Пример использования:
```python
import rectangle

# Вычисление площади прямоугольника
area_result = rectangle.area(3, 4)
print(area_result)  # Вернет 12
```

#### `perimeter(a, b)`

Функция принимает стороны прямоугольника `a` и `b` и возвращает периметр прямоугольника, рассчитанный по формуле `2 * (a + b)`

Пример использования:
```python
import rectangle

# Вычисление периметра прямоугольника
perimeter_result = rectangle.perimeter(3, 4)
print(perimeter_result)  # Вернет 14
```

### Квадрат `square.py`

#### `area(a)`

Функция принимает сторону квадрата `a` и возвращает площадь квадрата, рассчитанную по формуле `a²`

Пример использования:
```python
import square

# Вычисление площади квадрата
area_result = square.area(5)
print(area_result)  # Вернет 25
```

#### `perimeter(a)`

Функция принимает сторону квадрата `a` и возвращает периметр квадрата, рассчитанный по формуле `4a`

Пример использования:
```python
import square

# Вычисление периметра квадрата
perimeter_result = square.perimeter(5)
print(perimeter_result)  # Вернет 20
```

### Треугольник `triangle.py`

#### `area(a, h)`

Функция принимает основание `a` и высоту `h` треугольника и возвращает площадь треугольника, рассчитанную по формуле `a * h / 2`

Пример использования:
```python
import triangle

# Вычисление площади треугольника
area_result = triangle.area(3, 5)
print(area_result)  # Вернет 7.5
```

#### `perimeter(a, b, c)`

Функция принимает стороны треугольника `a`, `b` и `c` и возвращает периметр треугольника, рассчитанный по формуле `a + b + c`

Пример использования:
```python
import triangle

# Вычисление периметра треугольника
perimeter_result = triangle.perimeter(3, 4, 5)
print(perimeter_result)  # Вернет 12
```

## История изменений

|   Hash  |                Commit message               |     Date     |
|:-------:|:--------------------------------------------|-------------:|
| 8ba9aeb | Circle and square added                     |  Mar 4, 2021 |
| d078c8d | Docs added                                  |  Mar 4, 2021 |
| de708de | Added rectangle.py                          | Sep 11, 2023 |
| d8b2d68 | Added triangle.py                           | Sep 11, 2023 |
| f2f7a63 | Fixed perimeter calculation in rectangle.py | Sep 11, 2023 |
