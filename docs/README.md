# Geometric Lib

# Описание
В репозитории реализованы функции для расчета площади и периметра различных фигур: круга, квадрата, прямоугольника и треугольника.

# Используемые формулы

## Площадь
- Круг: S = πR² (R - радиус)
- Прямоугольник: S = ab (a, b - стороны)
- Квадрат: S = a² (a - сторона)
- Треугольник: S = ah (a - основание, h - высота)

## Периметр
- Круг: P = 2πR (R - радиус)
- Прямоугольник: P = 2a + 2b (a, b - стороны)
- Квадрат: P = 4a (a - сторона)
- Треугольник: P = a + b + c (a, b, c - стороны)


## Описание функций с примерами использования

## **circle.py**
- area: Принимает радиус круга r, возвращает площадь круга
```python
import circle
print(circle.area(1)) 
```

- perimeter: Принимает радиус круга r, возвращает периметр круга
```python
import circle
print(circle.perimeter(1)) 
```

## **square.py**
- area: Принимает сторону квадрата a, возвращает площадь квадрата
```python
import square
print(square.area(2)) 
```

- perimeter: Принимает сторону квадрата а, возвращает периметр квадрата
```python
import square
print(square.perimeter(3)) 
```

## **rectangle.py**
- area: Принимает стороны прямоугольника a и b, возвращает площадь прямоугольника
```python
import rectangle
print(rectangle.area(2, 3)) 
```

- perimeter: Принимает стороны прямоугольника а и b, возвращает периметр прямоугольника
```python
import rectangle
print(rectangle.perimeter(3, 4)) 
```

## **triangle.py**
- area: Принимает сторону треугольника a и высоту h, возвращает площадь треугольника 
```python
import triangle
print(triangle.area(1, 3)) 
```

- perimeter: Принимает стороны треугольника a, b и c, возвращает периметр треугольника
```python
import triangle
print(triangle.perimeter(5, 2)) 
```