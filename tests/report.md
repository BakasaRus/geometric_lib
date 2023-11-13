# Отчёт

1. [Цели и задачи тестирования](#1-цели-и-задачи-тестирования)
2. [Описание тестируемого продукта](#2-описание-тестируемого-продукта)
3. [Область тестирования](#3-область-тестирования)
4. [Стратегия тестирования](#4-стратегия-тестирования)
5. [Критерии приёмки](#5-критерии-приёмки)
6. [Результаты](#6-результаты)
    
    * [Ожидаемые результаты](#ожидаемые-результаты)

    * [Фактические результаты](#фактические-результаты)
    
        * [Метрики](#метрики)

        * [Выявленные дефекты](#выявленные-дефекты)

    * [Вердикт](#вердикт)
## 1. Цели и задачи тестирования
><b>Проверка функциональности библиотеки geometric_lib</b>:
проверка корректности вычисления периметров и площадей геометрических фигур.

## 2. Описание тестируемого продукта

Библиотека geometric_lib состоит из 4 файлов:

- circle.py

- rectangle.py

- square.py

- triangle.py

 В каждом из файлов для соответствующей фигуры существует функция area() для вычисления площади фигуры и функция perimeter() для вычисления периметра фигуры.

## 3. Область тестирования
### circle.py
- функция <b>area</b>

    Параметр <b>r</b> - радиус круга<br>
    Возвращает площадь круга (int/float)
   
   ```python
   print(area(408750))
   ```
- функция <b>perimeter</b>
    Параметр <b>r</b>  - радиус круга<br>
    Возвращает периметр круга (int/float)

   ```python
   print(perimiter(408750))
   ```
### rectangle.py
- функция <b>area</b>

    Параметры <b>a, b</b> - длина и ширина прямоугольника<br>
    Возвращает площадь прямоугольника

  ```python
  print(area(408, 750))
  ```

- функция <b>perimeter</b>

    Параметры <b>a, b</b> - длина и ширина прямоугольника<br>
    Возвращает периметр прямоугольника

    ```python
    print(perimter(408, 750))
    ```

### square.py

- функция <b>area</b>
    
    Takes <b>a</b> - side, returns area
   
   ```python
   print(area(3))
   ```
- функция <b>perimeter</b>

   Takes <b>a</b>  - side, returns perimeter of the square

   ```python
   print(perimeter(3))
   ```

### triangle.py

- функция <b>area</b>
    
    Параметры <b>a, h</b> - основание и высота треугольника
    ```python
    print(area(2, 5))
    ```

- функция <b>perimeter</b>

    Takes <b>a, b, c</b> - sides of the triangle, returns perimeter

    ```python 
    print(perimeter(4, 4, 4))
    ```

## 4. Стратегия тестирования
### Тип тестирования
- <b>функциональное<b>: модульное тестирование функций библиотеки.

### Планирование

- Определение различных сценариев работы библиотеки и в соответствии с ними определение различных случаев тестирования.

### Написание тестов

- Для данного тестирования будет использована библиотека unittest языка python, она позволяет тестировать отдельные функции. 
- Каждая группа тестов написана в отдельных классах, наследованных от базового класса unittest.TestCase. 
- Имена всех функций, являющихся тестами, начинаются с ключевого слова test.
- Внутри функций будут находиться вызовы операторов сравнения assertX (assertEqual, assertGreater и т. д.), они будут проверять полученные значения на соответствие заявленным.

- <b>Исполнение тестов</b>

> Тестирование запускается командой  ```python -m unittest tests/*.py ```

## 5. Критерии приёмки

|Сценарий|Требуемый результат|
|:--------:|:--------------------:|
|Пользователь вводит корректные данные| Функция возвращает ожидаемый результат|
|Пользователь вводит некорректные данные| Функция возвращает 0 или выбрасывается исключение TypeError|


## 6. Итоговые результаты
### Ожидаемые результаты
Функции модулей будут вызывать ошибки при попытке запуска функции с нечисловыми параметрами, будут возвращать неправильные ответы для отрицательных и нулевых числовых параметров

## Фактические результаты
### Метрики
| | |
|---------------|-----------|
|<b>Запущено</b>| 53 теста |
|<font color="green"><b>Пройдено</b></font>| 36 тестов, 68%|
|<font color="red"><b>Провалено</b></font>| 17 тестов, 32%|
|<b>Общее время</b>| 0.004 сек.|
| | |

### Проваленные тесты (результат тестирования)
```python
.F.....F.....FF..F....FF....FF.F.....F..F.FF....FF..F
======================================================================
FAIL: test_negative (tests.test_circle_area.CircleAreaTestCase.test_negative)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_circle_area.py", line 24, in test_negative
    self.assertEqual(res, 0)
AssertionError: 3.141592653589793 != 0

======================================================================
FAIL: test_negative (tests.test_circle_perimeter.CirclePerimeterTestCase.test_negative)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_circle_perimeter.py", line 24, in test_negative
    self.assertEqual(res, 0)
AssertionError: -12.566370614359172 != 0

======================================================================
FAIL: test_negative (tests.test_rectangle_area.RectangleAreaTestCase.test_negative)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_rectangle_area.py", line 32, in test_negative
    self.assertEqual(res, 0)
AssertionError: -3 != 0

======================================================================
FAIL: test_negative_both (tests.test_rectangle_area.RectangleAreaTestCase.test_negative_both)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_rectangle_area.py", line 36, in test_negative_both
    self.assertEqual(res, 0)
AssertionError: 9 != 0

======================================================================
FAIL: test_string (tests.test_rectangle_area.RectangleAreaTestCase.test_string)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_rectangle_area.py", line 39, in test_string
    with self.assertRaises(TypeError):
AssertionError: TypeError not raised

======================================================================
FAIL: test_negative (tests.test_rectangle_perimeter.RectanglePerimeterTestCase.test_negative)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_rectangle_perimeter.py", line 32, in test_negative
    self.assertEqual(res, 0)
AssertionError: -64 != 0

======================================================================
FAIL: test_negative_both (tests.test_rectangle_perimeter.RectanglePerimeterTestCase.test_negative_both)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_rectangle_perimeter.py", line 36, in test_negative_both
    self.assertEqual(res, 0)
AssertionError: -68 != 0

======================================================================
FAIL: test_zero_height (tests.test_rectangle_perimeter.RectanglePerimeterTestCase.test_zero_height)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_rectangle_perimeter.py", line 7, in test_zero_height
    self.assertEqual(0, 4)
AssertionError: 0 != 4

======================================================================
FAIL: test_zero_width (tests.test_rectangle_perimeter.RectanglePerimeterTestCase.test_zero_width)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_rectangle_perimeter.py", line 11, in test_zero_width
    self.assertEqual(res, 0)
AssertionError: 16 != 0

======================================================================
FAIL: test_negative (tests.test_square_area.SquareAreaTestCase.test_negative)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_square_area.py", line 24, in test_negative
    self.assertEqual(res, 0)
AssertionError: 4 != 0

======================================================================
FAIL: test_negative (tests.test_square_perimeter.SquarePerimeterTestCase.test_negative)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_square_perimeter.py", line 23, in test_negative
    self.assertEqual(res, 0)
AssertionError: -8 != 0

======================================================================
FAIL: test_string (tests.test_square_perimeter.SquarePerimeterTestCase.test_string)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_square_perimeter.py", line 26, in test_string
    with self.assertRaises(TypeError):
AssertionError: TypeError not raised

======================================================================
FAIL: test_negative_height (tests.test_triangle_area.TriangleAreaTestCase.test_negative_height)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_triangle_area.py", line 24, in test_negative_height
    self.assertEqual(res, 0)
AssertionError: -4.0 != 0

======================================================================
FAIL: test_negative_side (tests.test_triangle_area.TriangleAreaTestCase.test_negative_side)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_triangle_area.py", line 20, in test_negative_side
    self.assertEqual(res, 0)
AssertionError: -84.0 != 0

======================================================================
FAIL: test_impossible_sides (tests.test_triangle_perimeter.TrianglePerimeterTestCase.test_impossible_sides)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_triangle_perimeter.py", line 12, in test_impossible_sides
    self.assertEqual(res, 0)
AssertionError: 13 != 0

======================================================================
FAIL: test_negative (tests.test_triangle_perimeter.TrianglePerimeterTestCase.test_negative)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_triangle_perimeter.py", line 20, in test_negative
    self.assertEqual(res, 0)
AssertionError: 5 != 0

======================================================================
FAIL: test_zero_side (tests.test_triangle_perimeter.TrianglePerimeterTestCase.test_zero_side)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/admin/github-classroom/is-itmo-se-23/geometric_lib/tests/test_triangle_perimeter.py", line 8, in test_zero_side
    self.assertEqual(res, 0)
AssertionError: 6 != 0

----------------------------------------------------------------------
Ran 53 tests in 0.004s

FAILED (failures=17)
```
### Выявленные дефекты
|Модуль | Дефекты|
|-|-|
|circle.area| не учитывается случай отрицательного параметра и случай, когда параметр не является числом|
|circle.perimeter| не учитывается случай отрицательного параметра и случай, когда параметр не является числом|
|rectangle.area| не учитывается случай отрицательного параметров и случай, когда параметр не является числом|
|rectangle.perimeter| не учитывается случай отрицательного параметров и случай, когда параметр не является числом|
|square.area| не учитывается случай отрицательного параметра и случай, когда параметр не является числом|
|square.perimeter| не учитывается случай отрицательного параметра и случай, когда параметр не является числом|
|triangle.area| не учитывается случай отрицательного параметров и случай, когда параметр не является числом|
|triangle.perimeter| не учитывается случай отрицательного параметров, случай, когда параметр не является числом и случай, когда из трех сторон невозможно составить треугольник|

### Вердикт
Ни один модуль не удовлетворяет критериям приёма, так как при попытке использования некорректных данных ни выводится сообщение об ошибке, ни выбрасывается исключение, ни возвращается ненулевой код возврата.