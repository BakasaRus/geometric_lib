# Нахождение площади и периметра фигур

## Описание
В этом репозитории находятся различные функции на языке Python для нахождения площадей и периметров фигур. 

## Формулы
### Площадь
- Круг/окружность: `S = πR²` *(R - радиус)*
- Прямоугольник: `S = ab` *(a, b - стороны)*
- Квадрат: `S = a²` *(a - сторона)*
- Треугольник: `S = ah` *(a - основание, h - высота)*

### Периметр
- Круг/окружность: `P = 2πR` *(R - радиус)*
- Прямоугольник: `P = 2a + 2b` *(a, b - стороны)*
- Квадрат: `P = 4a` *(a - сторона)*
- Треугольник: `S = a + b + c` *(a, b, c - стороны)*

## Примеры вызова функций
### Площадь
- Круг/окружность:

```python
from geometric_lib import circle
r = float(input("Input circle radius: "))
print(f"Circle with radius {r} has area {circle.area(r)}")
```

- Прямоугольник:

```python
from geometric_lib import rectangle
a = float(input("Input the first side of the rectangle: "))
b = float(input("Input the second side of the rectangle: "))
print(f"Rectangle with sides {a} and {b} has area {rectangle.area(a, b)}")
```

- Квадрат:

```python
from geometric_lib import square
a = float(input("Input square side: "))
print(f"Square with side {a} has area {square.area(a)}")
```

- Треугольник:

```python
from geometric_lib import triangle
a = float(input("Input triangle side: "))
h = float(input("Input triangle height: "))
print(f"Triangle with side {a} and height {h} has area {square.area(a)}")
```

### Периметр
- Круг/окружность: 

```python
from geometric_lib import circle
r = float(input("Input circle radius: "))
print(f"Circle with radius {r} has perimeter {circle.perimeter(r)}")
```

- Прямоугольник:

```python
from geometric_lib import rectangle
a = float(input("Input the first side of the rectangle: "))
b = float(input("Input the second side of the rectangle: "))
print(f"Rectangle with sides {a} and {b} has perimeter {rectangle.perimeter(a, b)}")
```

- Квадрат:

```python
from geometric_lib import square
a = float(input("Input square side: "))
print(f"Square with side {a} has perimeter {square.perimeter(a)}")
```

- Треугольник:

```python
from geometric_lib import triangle
a = float(input("Input the first side of the triangle: "))
b = float(input("Input the second side of the triangle: "))
c = float(input("Input the third side of the triangle: "))
print(f"Triangle with sides {a}, {b}, {c} has perimeter {triangle.perimeter(a)}")
```

## История коммитов
HASH | описание
--- | ---
`8ba9aeb3cea847b63a91ac378a2a6db758682460` | Добавлены функции для круга/окружности и квадрата
`d078c8d9ee6155f3cb0e577d28d337b791de28e2` | Добавлена документация 
`690a2b0c874e8478f031fb323ea8c1ac4649a43e` | Добавлены функции для прямоугольника 
`88e3b90b9f17dd0bad67faf3297a9f163fe16aa5` | Добавлены функции для треугольника и исправлена функция периметра для прямоугольника
`6fb74e17f0e298ff3cd5e7901ef096be305f143c` | Обновлён README.md
`20b5c9f7fdb586276dcd3440a37d65f1124b9427` | Добавлены комментарии к функциям
`a90b1eced2f4dcb5f73e92f1c5e2099075636d4a` | Добавлены примеры в README.md
`e929703be17f6ae81674d5fb19b205fc89f89495` | Добавлено тестирование с помощью библиотеки unittest
`0a22368018be89806e58b0535bcaed44f837aee5` | Обновлён README.md
`b02cf552e51dafe1ebab3e2411ae6530aed55842` | Исправлены тесты