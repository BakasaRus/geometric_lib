# Math formulas
## Area
- Circle: $S = \pi R^2$
- Rectangle: $S = ab$
- Square: $S = a^2$

## Perimeter
- Circle: $P = 2\pi R$
- Rectangle: $P = 2a + 2b$
- Square: $P = 4a$

# Project description
 This project is aimed at working with ___geometric shapes and performing operations on them.___

# Functions for working with geometric objects

## Circle
- ***Area***: Принимает радиус круга и возвращает его площадь

  Вызов программы
  ```
  from circle.py import *
  print(area(3))
  ``` 
  выведет __28.26...__

- ***Perimeter***: Принимает радиус круга и возвращает длину его окружности

  Вызов программы
  ```
  from circle.py import *
  print(perimeter(3))
  ```
  выведет __18.84...__

## Rectangle
- ***Area***: Принимает длины сторон прямоугольника и возвращает его площадь

  Вызов программы
  ```
  from rectangle.py import *
  print(area(3, 4))
  ``` 
  выведет __12__

- ***Perimeter***: Принимает длины сторон прямоугольника и возвращает его периметр

  Вызов программы
  ```
  from rectangle.py import *
  print(perimeter(3, 4))
  ``` 
  выведет __14__

## Square
- ***Area***: Принимает длину стороны квадрата и возвращает его площадь

  Вызов программы
  ```
  from square.py import *
  print(area(5))
  ``` 
  выведет __25__

- ***Perimeter***: Принимает длину стороны квадрата и возвращает его периметр

  Вызов программы
  ```
  from square.py import *
  print(perimeter(3))
  ``` 
  выведет __20__
  
## Triangle
- ***Area***: Принимает длину стороны треугольника и высоты, опущенную на данную сторону, и возвращает его площадь

  Вызов программы
  ```
  from triangle.py import *
  print(area(3, 4))
  ``` 
  выведет __6__

- ***Perimeter***: Принимает длины трёх сторон треугольника и возвращает его площадь

  Вызов программы
  ```
  from triangle.py import *
  print(perimeter(1, 5, 8))
  ``` 
  выведет  __14__

# Сhanges in the project
| Hash of the commit | Changes                                                                               |
| ------------------ | ------------------------------------------------------------------------------------- |
|***8ba9aeb***       | Создание файлов `circle.py` и `square.py`                                             |
| ***d078c8d***      | Создание каталога `docs` с файлом `READ.md` с начальной документацией по проекту      |
| ***fbf478e***      | Создание новой ветки ***"new_features_408353"***, создание файла `rectangle.py`       |
| ***ac590c9***      | Создание файла `triangle.py` и исправление функции `perimeter` в файле `rectangle.py` |
| ***1ece8f5***      | Написание документации к функциям                                                     |
