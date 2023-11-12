# Отчёт о тестировании

## 1. Цели и задачи тестирования

Целью тестирования является проверка корректности функций вычисления площади и периметра геометрических фигур,
реализованных в модулях *circle*, *rectangle*, *square* и *triangle*, представленных в библиотеке **geometric_lib.**

## 2. Описание тестируемого продукта

Библиотека **geometric_lib** состоит из 4 файлов:

- `circle.py`
  - 
    - `area(radius)`
    - `perimeter(radius)`

- `rectangle.py`
  - 
    - `area(width, height)`
    - `perimeter(width, height)`

- `square.py`
  -
    - `area(width)`
    - `perimeter(width)`

- `triangle.py`
  - 
    - `area(side, height)`
    - `perimeter(side_a, side_b, side_c)`

Каждый из файлов библиотеки содержит два функции. Первая считает площадь геометрической фигуры
по переданным данным, а вторая - периметр.

## 3. Область тестирования

### Circle.py

- Square: `area(radius)` \
  \- Takes the radius of a circle, returns the area of ​​the circle of the given radius \
  _Example:_

```
from circle import area

>>> print(area(3))
28.274333882308138
```

- Perimeter: `perimeter(radius)` \
  \- Takes the radius of a circle, returns the perimeter of ​​the circle of the given radius \
  _Example:_

```
from circle import perimeter

>>> print(perimeter(3))
18.84955592153876
```

### Rectangle.py

- Square: `area(width, height)` \
  \- Takes the width and length of a rectangle, returns the area of ​​the corresponding rectangle \
  _Example:_

```
from rectangle import area

>>> print(area(3, 5))
15
```

- Perimeter: `perimeter(width, height)` \
  \- Takes the width and length of a rectangle, returns the perimeter of ​​the corresponding rectangle \
  _Example:_

```
from rectangle import perimeter

>>> print(perimeter(3, 5)) 
16
```

### Square.py

- Square: `area(width)` \
  \- Takes the side length of a square, returns the area of ​​the corresponding square \
  _Example:_

```
from square import area

>>> print(area(3))
9
```

- Perimeter: `perimeter(width)` \
  \- Takes the side length of a square, returns the perimeter of ​​the corresponding square \
  _Example:_

```
from square import perimeter

>>> print(perimeter(3))
12
```

### Triangle.py

- Square: `area(side, height)` \
  \- Takes the side length and height of a triangle, returns the area of ​​the corresponding triangle \
  _Example:_

```
from triangle import area

>>> print(area(3, 4)) 
6
```

- Perimetr: `perimeter(side_a, side_b, side_c)` \
  \- Takes the side length and height of a triangle, returns the perimeter of ​​the corresponding triangle \
  _Example:_

```
from triangle import perimeter

>>> print(perimeter(3, 4, 5))
12
```

## 4. Стратегия тестирования

Тип тестирования, который использовался в данном случае, называется *функциональное тестирование*.
Оно подразумевает под собой модульное тестирование каждой функции библиотеки **geometric_lib**

#### Создание тестов

Для тестирования использовалась библиотека unittest. Она позволяет создать отдельную группу тестов
для каждой функции и проверить корректность ее работы в различных сценариях. Для этого создается класс,
наследуемый от unittest.TestCase, в функциях которого прописываются разнообразные входные данные и предполагаемые
результаты.
Вердикт определяется с помощью функции `assertEqual(result, expected_result)`, в которую передаются результат работы
функции
и ожидаемый результат. Она их сравнивает и выводит в консоль вердикт прохождения теста.

## 5. Критерии приемки

|                 Условия                  |                             Ожидаемый результат                              |
|:----------------------------------------:|:----------------------------------------------------------------------------:|
| Функция обрабатывает некорректные данные | Функция возвращает сообщение об некорректности введенных данных пользователю |
|  Функция обрабатывает корректные данные  |                       Функция выводит результат работы                       |

## 6. Результаты

### Ожидаемые результаты

Тесты с отрицательными, а в некоторых случаях еще и с нулевыми, входными данными будут провалены,
так как подобные сценарии не обрабатываются в функциях

## Фактические результаты

|        Модуль         | Пройдено | Провалено |
|:---------------------:|:--------:|:---------:|
|     circle.area()     |    3     |     1     |
|  circle.perimeter()   |    3     |     1     |
|   rectangle.area()    |    4     |     1     |
| rectangle.perimeter() |    3     |     2     |
|     square.area()     |    3     |     1     |
|  square.perimeter()   |    3     |     1     |
|    triangle.area()    |    3     |     2     |
| triangle.perimeter()  |    3     |     1     |

### Выявленные дефекты

| Функция             | Дефекты                                                        |
|:--------------------|:---------------------------------------------------------------|
| circle.area         | некорректная обработка случая отрицательного радиуса           |
| circle.perimeter    | некорректная обработка случая отрицательного радиуса           |
| rectangle.area      | некорректная обработка случая отрицательной стороны            |
| rectangle.perimeter | некорректная обработка случая неположительной стороны          |
| square.area         | некорректная обработка случая отрицательной стороны            |
| square.perimeter    | некорректная обработка случая отрицательной стороны            |
| triangle.area       | некорректная обработка случая неположительной высоты и стороны |
| triangle.perimeter  | некорректная обработка случая неположительной стороны          |

### Вердикт
 Проект требует доработки. В каждую из функций требуется добавить обработчик некорректных
 входных данных, который будет возвращать сообщение для пользователя о недопустимости входных данных.