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
|Пользователь вводит некорректные данные| Функция выбрасывает исключение ValueError|


## 6. Итоговые результаты
### Ожидаемые результаты
Функции модулей будут вызывать ошибки при попытке запуска функции с нечисловыми параметрами, будут возвращать неправильные ответы для отрицательных и нулевых числовых параметров

## Фактические результаты
### Метрики
| | |
|---------------|-----------|
|<b>Запущено</b>| 53 теста |
|<font color="green"><b>Пройдено</b></font>| 28 тестов, 53%|
|<font color="red"><b>Провалено</b></font>| 25 тестов, 47%|
|<b>Общее время</b>| 0.007 сек.|
| | |


```
.E..E..E..E..EE..E....EE..EEEE.E..E..E..EEEE.E..EE.EE
```

### Проваленные тесты

* ERROR: test_negative (tests.test_circle_area.CircleAreaTestCase.test_negative)
* ERROR: test_string (tests.test_circle_area.CircleAreaTestCase.test_string)
* ERROR: test_negative (tests.test_circle_perimeter.CirclePerimeterTestCase.test_negative)
* ERROR: test_string (tests.test_circle_perimeter.CirclePerimeterTestCase.test_string)
* ERROR: test_negative (tests.test_rectangle_area.RectangleAreaTestCase.test_negative)
* ERROR: test_negative_both (tests.test_rectangle_area.RectangleAreaTestCase.test_negative_both)
* ERROR: test_string (tests.test_rectangle_area.RectangleAreaTestCase.test_string)
* ERROR: test_negative (tests.test_rectangle_perimeter.RectanglePerimeterTestCase.test_negative)
* ERROR: test_negative_both (tests.test_rectangle_perimeter.RectanglePerimeterTestCase.test_negative_both)
* ERROR: test_string (tests.test_rectangle_perimeter.RectanglePerimeterTestCase.test_string)
* ERROR: test_zero_both (tests.test_rectangle_perimeter.RectanglePerimeterTestCase.test_zero_both)
* ERROR: test_zero_height (tests.test_rectangle_perimeter.RectanglePerimeterTestCase.test_zero_height)
* ERROR: test_zero_width (tests.test_rectangle_perimeter.RectanglePerimeterTestCase.test_zero_width)
* ERROR: test_negative (tests.test_square_area.SquareAreaTestCase.test_negative)
* ERROR: test_string (tests.test_square_area.SquareAreaTestCase.test_string)
* ERROR: test_negative (tests.test_square_perimeter.SquarePerimeterTestCase.test_negative)
* ERROR: test_string (tests.test_square_perimeter.SquarePerimeterTestCase.test_string)
* ERROR: test_zero (tests.test_square_perimeter.SquarePerimeterTestCase.test_zero)
* ERROR: test_negative_height (tests.test_triangle_area.TriangleAreaTestCase.test_negative_height)
* ERROR: test_negative_side (tests.test_triangle_area.TriangleAreaTestCase.test_negative_side)
* ERROR: test_string (tests.test_triangle_area.TriangleAreaTestCase.test_string)
* ERROR: test_impossible_sides (tests.test_triangle_perimeter.TrianglePerimeterTestCase.test_impossible_sides)
* ERROR: test_negative (tests.test_triangle_perimeter.TrianglePerimeterTestCase.test_negative)
* ERROR: test_string (tests.test_triangle_perimeter.TrianglePerimeterTestCase.test_string)

* ERROR: test_zero_side (tests.test_triangle_perimeter.TrianglePerimeterTestCase.test_zero_side)

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