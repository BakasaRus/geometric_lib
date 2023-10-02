# Geometric Lib

Данный проект содержит четыре файла: circle.py, rectangle.py, square.py, triangle.py. Каждый файл содержит функции, позволяющие найти периметр и площадь соотвествующей названию файла геометрической фигуры.

Рассмотрим подробнее функционал каждого файла:

## **circle.py**

### *Функции*

- def area(r) принимает радиус круга r и возвращает площадь круга соответствующего радиуса<br>
- def perimeter(r) принимает радиуса окружности r и возвращает площадь круга радиуса r

### *Примеры*

```python
print(area(7))
```
Вывод: 49π<br>
```python
print(perimeter(4))
```
Вывод: 8π<br>

## **rectangle.py**

### *Функции*

- def area(a, b) принимает длину и ширину прямоугольника и возвращает площадь<br>
- def perimeter(a, b) принимает длину и ширину прямоугольника и возвращает периметр прямоугольника

### *Примеры*

```python
print(area(7, 4))
``` 
Вывод: 28<br>
```python
print(perimeter(4, 3))
```
Вывод: 14<br>

## **square.py**

### *Функции*

- def area(a): принимает длину стороны квадрата и возвращает площадь квадрата<br>
- def perimeter(a): принимает длину стороны квадрата и возвращает периметр квадрата

### #*Примеры*
```python
print(area(7))
```
Вывод 49<br>
```python
print(perimeter(5))
```
Вывод: 20<br>

## **triangle.py**

### *Функции*

- def area(a, h) принимает длину основания и высоту треугольника и возвращает площадь треугольника<br>
- def perimeter(a, b, c) принимает три стороны треугольника и возвращает периметр треугольника

### *Примеры*

```python
print(area(7, 4))
```
Вывод: 14<br>
```python
print(perimeter(4, 4, 4))
```
Вывод: 12<br>

## Математические формулы
### *Площадь*
- Circle: S = πR²<br>
- Rectangle: S = ab<br>
- Square: S = a²<br>

### *Периметр*
- Circle: P = 2πR<br>
- Rectangle: P = 2a + 2b<br>
- Square: P = 4a<br>

## *История коммитов*
* d987557 (HEAD -> lab_2, origin/lab_2) README.md updated
* 3f7b892 Update python files function description, readme.md
* b8f1c04 (origin/main, origin/HEAD, main) Edit file
* b08a51b Add file
* d078c8d L-03: Docs added
* 8ba9aeb L-03: Circle and square added
