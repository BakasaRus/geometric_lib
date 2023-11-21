# Отчёт тестирования

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
- <b>function</b> area

   Takes <b>r</b> - radius, returns area
   
   ```python
   print(area(3))
   ```
- <b>function</b> perimeter

   Takes <b>r</b>  - radius, returns perimeter of the circle

   ```python
   print(perimiter(3))
   ```
### rectangle.py
- <b>function</b> area

  Takes <b>a, b</b>- length of sides of the rect, returns area

  ```python
  print(area(3, 4))
  ```

- <b>function</b> perimeter

    Takes <b>a, b</b>- length of sides of the rect, returns perimeter

    ```python
    print(perimter(3, 4))
    ```

### square.py

- <b>function</b> area
    
    Takes <b>a</b> - side, returns area
   
   ```python
   print(area(3))
   ```
- <b>function</b> perimeter

   Takes <b>a</b>  - side, returns perimeter of the square

   ```python
   print(perimeter(3))
   ```

### triangle.py

- <b>function</b> area
    
    Takes <b>a, h</b> - side and height of the triangle, returns area

    ```python
    print(area(2, 4))
    ```

- <b>function</b> perimeter

    Takes <b>a, b, c</b> - sides of the triangle, returns perimeter

    ```python 
    print(perimeter(4, 4, 4))
    ```

## 4. Стратегия тестирования
 <b>Тип тестирования</b> - функциональное: модульное тестирование функций библиотеки.

- <b>Планирование</b>

>Определение различных сценариев работы библиотеки и в соответствии с ними определение различных случаев тестирования.

- <b>Написание тестов</b>

>Для данного тестирования будет использована библиотека unittest языка python, которая позволяет тестировать отдельные функции. Каждая группа тестов написана в отдельных классах, наследованных от базового класса unittest.TestCase. Имена всех функций, являющихся тестами, начинаются с ключевого слова test. Внутри функций должны быть вызовы операторов сравнения (assertX) — именно они будут проверять наши полученные значения на соответствие заявленным.

- <b>Исполнение тестов</b>

> Тестирование запускается командой  ```python -m unittest discover -s tests/ -p '*_tests.py' ```

## 5. Критерии приёмки
|Сценарий|Требуемый результат|
|:--------:|:--------------------:|
|Пользователь вводит корректные данные| Функция возвращает ожидаемый результат|
|Пользователь вводит некорректные данные| Функция выводит сообщение об ошибке и/или определённый код возврата (например -1)|


## 6. Результаты
### Ожидаемые результаты
Не будут пройдены тесты с отрицательными и нулевыми аргументами, поскольку такие случаи не предусмотрены в функциях.

## Фактические результаты
### Метрики
|||
|--------|-------------|
|<b>Запущено</b>| 42 теста |
|<font color="green"><b>Пройдено</b></font>| 18 тестов, 53%|
|<font color="red"><b>Провалено</b></font>| 17 тестов, 47%|
|<b>Общее время</b>| 0.004 сек.|

|Модуль| <font color="green">Пройдено</font> | <font color="red">Провалено</font>| Сообщение тестирующей системы|
|:-:|:-:|:-:|:-|
|circle.area| 3 | 2 | AssertionError: ValueError not raised by area<br>AssertionError: TypeError not raised by area|
|circle.perimeter| 4 | 1 | AssertionError: ValueError not raised by perimeter|
|rectangle.area| 4 | 2 | AssertionError: ValueError not raised by area<br>AssertionError: ValueError not raised by area|
|rectangle.perimeter| 3 | 2 | AssertionError: ValueError not raised by perimeter<br>AssertionError: ValueError not raised by perimeter|
|square.area| 4 | 2| AssertionError: ValueError not raised by area<br>AssertionError: ValueError not raised by area|
|square.perimeter| 4 | 2| AssertionError: ValueError not raised by perimeter<br>AssertionError: ValueError not raised by perimeter|
|triangle.area| 3 | 4 | AssertionError: ValueError not raised by area<br>AssertionError: ValueError not raised by area<br>AssertionError: ValueError not raised by area<br>AssertionError: ValueError not raised by area|
|triangle.perimeter| 3 | 2 | AssertionError: ValueError not raised by perimeter<br>AssertionError: ValueError not raised by perimeter|


### Выявленные дефекты
|Модуль | Дефекты|
|:-|:-|
|circle.area| некорректная обработка случая отрицательного радиуса<br>некорректная обработка неверного входного типа|
|circle.perimeter| некорректная обработка случая отрицательного радиуса|
|rectangle.area| некорректная обработка случая отрицательной стороны<br>некорректная обработка случая нулевой стороны|
|rectangle.perimeter| некорректная обработка случая отрицательной стороны<br>некорректная обработка случая нулевой стороны|
|square.area| некорректная обработка случая отрицательной стороны<br>некорректная обработка случая нулевой стороны|
|square.perimeter| некорректная обработка случая отрицательной стороны<br>некорректная обработка случая нулевой стороны|
|triangle.area| некорректная обработка случая отрицательной высоты<br>некорректная обработка случая отрицательной стороны<br>некорректная обработка случая нулевой стороны<br>некорректная обработка случая нулевой высоты|
|triangle.perimeter| некорректная обработка случая отрицательной стороны<br>некорректная обработка случая нулевой стороны|

### Вердикт
>Модули <b>не удовлетворяют</b> критериям приёма, поскольку при сценарии, когда пользователь вводит некорректные данные, функции не возвращают ни сообщение об ошибке.   
