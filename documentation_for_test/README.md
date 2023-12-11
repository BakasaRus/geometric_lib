# Документация для *unittest*

## 1) Цели тестирования

Цель тестирования заключается в проверке корректности работы функций расчета **площади** и **периметра** геометрических фигур, реализованных в модулях circle, rectangle, square, triangle. 

## 2) Описание тестируемого продукта

### **Circle**

#### *Main functions*

* `def area` Takes the variable *r* and returns the area of the circle

* `def perimeter` Takes the variable *r* and returns the perimeter of the circle

#### *Examples*

```python
import circle

print(circle.area(3))  # Print 28.274333882308138
print(circle.perimeter(3))  # Print 18.84955592153876

```

##

### **Square**

#### *Main functions*

* `def area` Takes the variable *a* and returns the square area

* `def perimeter` Takes the variable *a* and returns the perimeter of the square

#### *Examples*

```python
import square

print(square.area(9))  # Print 81
print(square.perimeter(9))  # Print 36

```

###

### **Rectangle**

#### *Main functions*

* `def area` Takes the variables *a* and *b* and returns the area of the rectangle

* `def perimeter` Takes the variables *a* and *b* and returns the perimeter of the rectangle

#### *Examples*

```python
import rectangle

print(rectangle.area(3, 4))  # Print 12
print(rectangle.perimeter(3, 4))  # Print 14

```

###

### **Triangle**

#### *Main functions*

* `def area` Takes the variables *a* and *h* and returns the area of the triangle

* `def perimeter`Takes three sides of a triangle *a*, *b*, *c* and returns its perimeter

#### *Examples*

```python
import triangle

print(triangle.area(4, 5))  # Print 10
print(triangle.perimeter(3, 4, 6))  # Print 13

```

## 3) Область тестирования:

### Тестирование будет иметь следующие аспекты:

1) Правильность расчета площади и периметра для различных размеров.
2) Обработка нулевых и отрицательных значений входных параметров.
3) Тестирование на очень больших чисел.

## 4) Стратегии тестирования

Применяем комбинированный подход, включающий в себя модульное тестирование каждого модуля по отдельности

Для каждого модуля будут проведены тесты на правильность расчетов, обработку ошибок и соответствие результатов ожидаемым значениям

## 5) Ожидаемый результат

#### Начертим таблицу

|       Модуль        | Количество пройденных тестов | Количество провальных тестов |                                                                                                                     
|:-------------------:|:----------------------------:|:----------------------------:|
|     circle.area     |              3               |              1               |                                                                                   
|  circle.perimeter   |              3               |              1               |                                                                                       
|   rectangle.area    |              3               |              1               | 
| rectangle.perimeter |              2               |              2               | 
|     square.area     |              3               |              1               |                                                                        
|  square.perimeter   |              2               |              1               |                                                                                
|    triangle.area    |              3               |              1               | 
| triangle.perimeter  |              2               |              2               | 

### Провалено 10 тесто

## Вывод

Hеверный ответ связан с тем, что мы неправильно считаем площадь и периметр для отрицательных и нулевых значений
