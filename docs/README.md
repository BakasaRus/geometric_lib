# Geometric library
Библиотека содержит набор функций для работы с различными геометрическими фигурами. На данный момент реализованы функции вычисления площади и периметра для следующих фигур: круг, квадрат, прямоугольник, треугольник, для треугольника реализована функция вычисления длины медианы.

## Фигуры

### Круг
#### Площадь
```python
area(r: float) -> float
```
Функция area() принимает радиус круга r и вычисляет его площадь.
Для вычисления используется формула:

$S = πr^2$

Пример использования:
```python
import circle

# area of a "ring" between two circles
r1 = float(input())
r2 = float(input())

A = circle.area(max(r1, r2)) - circle.area(min(r1, r2))
print("Area of the ring: " + A)
```
#### Периметр
```python
perimeter(r: float) -> float
```
Функция perimeter() принимает радиус окружности r и вычисляет её длину.
Для вычисления используется формула:

$P = 2πr$

Пример использования:
```python
import circle

r = float(input("Radius: "))
p = circle.perimeter(r)
print("Perimeter of the circle: " + p)
```

### Прямоугольник
#### Площадь
```python
area(a: float, b: float) -> float
```
Функция area() принимает стороны прямоугольника и вычисляет его площадь.
Для вычисления используется формула:

$S = ab$

Пример использования:
```python
import rectangle

a = float(input("a: "))
b = float(input("b: "))

print("Area: " + rectangle.area(a, b))
```

#### Периметр
```python
perimeter(a: float, b: float) -> float
```
Функция perimeter() принимает стороны прямоугольника и вычисляет его периметр.
Для вычисления используется формула:

$P = 2(a+b)$

Пример использования:
```python
import rectangle

a = float(input("a: "))
b = float(input("b: "))
p = rectangle.perimeter(a, b)

print("Perimeter of the rectangle: " + p)
```

### Квадрат
#### Площадь
```python
area(a: float) -> float
```
Функция area() принимает сторону квадрата и вычисляет его площадь.
Для вычисления используется формула:

$S = a^2$

Пример использования:
```python
import square

a = float(input("Side of square: "))
area = square.area(a)

print("Area of the square: " + area)
```
#### Периметр
```python
perimeter(a: float) -> float
```
Функция perimeter() принимает сторону квадрата и вычисляет его периметр.
Для вычисления используется формула:

$P = 4a$

Пример использования:
```python
import square

a = float(input("Side of square: "))
p = square.perimeter(a)

print("Perimeter of the square: " + p)
```

### Треугольник
#### Площадь
```python
area(a: float, h: float) -> float
```
Функция area() принимает сторону треугольника и вычисляет его площадь.
Для вычисления используется формула:

$S = \dfrac{ah}{2}$

Пример использования:
```python
import triangle

a = float(input("Side of triangle: "))
h = float(input("Altitude of triangle: "))
area = triangle.area(a, h)

print("Area of the triangle: " + area)
```

#### Периметр
```python
perimeter(a: float, b: float, c: float) -> float
```
Функция perimeter() принимает стороны треугольника и вычисляет его периметр.
Для вычисления используется формула:

$P = a + b + c$

Пример использования:
```python
import triangle

a = float(input("Side 1: "))
a = float(input("Side 2: "))
a = float(input("Side 3: "))
p = triangle.perimeter(a, b, c)

print("Perimeter of the triangle: " + p)
```

#### Длина медианы
```python
median(a: float, b: float, c: float) -> float
```
Функция median() принимает стороны треугольника a, b и c и вычисляет длину его медианы, проведённой к стороне a.
Для вычисления используется формула:

$m = \dfrac{\sqrt{2b^2 + 2c^2 - a^2}}{2}$

Пример использования:
```python
import triangle

a = float(input("Side 1: "))
a = float(input("Side 2: "))
a = float(input("Side 3: "))
p = triangle.media(a, b, c)

print("Length of the median: " + p)
```

## История изменений

|Событие                                                     |Дата      |Коммит                                  |
|------------------------------------------------------------|----------|----------------------------------------|
|Создание проекта                                            |03/04/2021|8ba9aeb3cea847b63a91ac378a2a6db758682460|
|Добавление раздела docs                                     |03/04/2021|d078c8d9ee6155f3cb0e577d28d337b791de28e2|
|Добавление функций для прямогульника                        |09/04/2023|dbbfec49ea17da1589f034ad8dc03418a807fa16|
|Добавление функций для треугольника                         |09/04/2023|e8928cf6dd206b39e6714b9496144df8f8322b4c|
|Исправление ошибки в вычислении периметра для прямоугольника|09/04/2023|476f3b3c3fd62d67fb962e673bfd53761d0e4192|
|Добавление функции вычисления медианы для треугольника      |09/21/2023|2f37286da940cdffc977388a1461f25603d97546|
|Исправление мелких ошибок                                   |09/21/2023|57f8c577673ecdcc25a0d8983800237c6ca15f40|
|Добавление тестов                                           |11/12/2023|589bfcf1ff4bb303eb08662c96618da25165a6f3|
|Дополнение тестов                                           |11/21/2023|589bfcf1ff4bb303eb08662c96618da25165a6f3|
