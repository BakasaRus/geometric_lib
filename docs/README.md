# Geometric Lib

# Описание
В репозитории реализованы функции для расчета площади и периметра различных фигур: круга, квадрата, прямоугольника и треугольника.

# Используемые формулы

## Площадь
- Круг: $S = \pi R^2$ ($R$ - радиус)
- Прямоугольник: $S = ab$ ($a$, $b$ - стороны)
- Квадрат: $S = a^2$ ($a$ - сторона)
- Треугольник: $S = ah$ ($a$ - основание, $h$ - высота)

## Периметр
- Круг: $P = 2 \pi R$ ($R$ - радиус)
- Прямоугольник: $P = 2a + 2b$ ($a$, $b$ - стороны)
- Квадрат: $P = 4a$ ($a$ - сторона)
- Треугольник: $P = a + b + c$ ($a$, $b$, $c$ - стороны)


## Описание функций с примерами использования

## **circle.py**
- area: Принимает радиус круга $r$, возвращает площадь круга
```python
import circle
print(circle.area(1)) 
```

- perimeter: Принимает радиус круга $r$, возвращает периметр круга
```python
import circle
print(circle.perimeter(1)) 
```

## **square.py**
- area: Принимает сторону квадрата $a$, возвращает площадь квадрата
```python
import square
print(square.area(2)) 
```

- perimeter: Принимает сторону квадрата $а$, возвращает периметр квадрата
```python
import square
print(square.perimeter(3)) 
```

## **rectangle.py**
- area: Принимает стороны прямоугольника $a$ и $b$, возвращает площадь прямоугольника
```python
import rectangle
print(rectangle.area(2, 3)) 
```

- perimeter: Принимает стороны прямоугольника $а$ и $b$, возвращает периметр прямоугольника
```python
import rectangle
print(rectangle.perimeter(3, 4)) 
```

## **triangle.py**
- area: Принимает сторону треугольника $a$ и высоту $h$, возвращает площадь треугольника 
```python
import triangle
print(triangle.area(1, 3)) 
```

- perimeter: Принимает стороны треугольника $a$, $b$ и $c$, возвращает периметр треугольника
```python
import triangle
print(triangle.perimeter(5, 2, 4)) 
```

## *История проекта*


- commit `c52d88f4671bf47c966daecf2f35ab27f60138ea` (HEAD -> lab2) added documentation

- commit `cc69822b4053d376be5ab2a95c2d62ef4f250e64` added function descriptions

- commit `b7c5abe76ef68f143beb001dc88af01173f66936` (main) fixed error in rectangle.py

- commit `405e201ba15cdbad928afce2bf99a25c41e2c1e5` new file triangle.py added

- commit `5d906e562cb46afbf8be6bd6edc8c904e28aef5d` new file rectangle.py added

- commit `d078c8d9ee6155f3cb0e577d28d337b791de28e2` (origin/main, origin/HEAD) L-03: Docs added

- commit `8ba9aeb3cea847b63a91ac378a2a6db758682460` L-03: Circle and square added
  
