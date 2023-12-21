# Документация по тестированию **unittest**

## 1) Цели тестирования

#### Цель тестирования заключается в проверке корректности работы функций геометрических фигур : (*area*, *perimeter*) библиотеки *geometric_lib*, реализованных в модулях circle, rectangle, square, triangle.

## 2) Описание тестируемого продукта

### Библиотека *geometric_lib* состоит из 4 модулей:
 
### *Circle*

#### *functions*

* `def area` возращает площадь круга

* `def perimeter` возращает периметр круга

#### *Examples*

```python
import circle

print(circle.area(2))  # print 12.56
print(circle.perimeter(2))  # print 12.56
```

### *Square*

#### *functions*

* `def area`возращает площадь квадрата

* `def perimeter`возращает периметр квадрата

#### *Examples*

```python
import square

print(square.area(3))  # Print 9
print(square.perimeter(3))  # Print 12
```

### *Rectangle*

#### *functions*

* `def area` возращает площадь прямоугольника

* `def perimeter` возращает периметр прямоугольника

#### *Examples*

```python
import rectangle

print(rectangle.area(3, 4))  # Print 12
print(rectangle.perimeter(3, 4))  # Print 14
```

### *Triangle*

#### *functions*

* `def area` возращает площадь треугольника

* `def perimeter` возращает периметр треугольника

#### *Examples*

```python
import triangle

print(triangle.area(2, 5))  # Print 5
print(triangle.perimeter(3, 4, 5))  # Print 12
```

## 3) Область тестирования:

### Тестирование будет иметь следующие аспекты:

* #### Правильность расчета площади и периметра для различных данных.
* #### Обработка некоректных значений входных данных.

## 4) Стратегии тестирования

**Тип тестирования** - *функциональное*: модульное тестирование.

* *Планирование*

Определение поведения функций в зависимости от различных входных данных.

* *Написание тестов*

Для тестирования будет использована библиотека *unittest* из языка *python*, которая позволяет тестировать отдельные функции.

* *Исполнение тестов*

Тестирование запускается командой  ```python -m unittest tests/tests.py ```

## 5) Ожидаемый результат

|       Функции       | Количество пройденных тестов | Количество провальных тестов |
|:-------------------:|:----------------------------:|:----------------------------:|
|     circle.area     |              3               |              1               |
|  circle.perimeter   |              3               |              1               |
|   rectangle.area    |              3               |              1               |
| rectangle.perimeter |              2               |              2               |
|     square.area     |              3               |              1               |
|  square.perimeter   |              3               |              1               |
|    triangle.area    |              3               |              1               |
| triangle.perimeter  |              2               |              2               |

### Пройдено 22 теста | Провалено 10 тестов

## Вывод

### Hеверный ответ связан с тем, что мы не обрабатываем введение некоректных данных.