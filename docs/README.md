# geometric_lib

Библиотека включает в себя функции расчета площади и периметра для четырех геометрических фигур: круга, прямоугольника, квадрата, треугольника.

## Area
- Circle: $S = \pi R^2$
- Rectangle: $S = ab$
- Square: $S = a^2$
- Triangle: $S = \frac{ah}{2}$

## Perimeter
- Circle: $P = 2 \pi R$
- Rectangle: $P = 2a + 2b$
- Square: $P = 4a$
- Triangle: $P = a + b + c$

## Файлы 

- `rectangle.py` -- расчеты для фигуры Прямоугольник
- `square.py` -- расчеты для фигуры Квадрат
- `сircle.py` -- расчеты для фигуры Круг
- `triangle.py` -- расчеты для фигуры Треугольник

### [rectangle.py](../rectangle.py)
- **`area(a, b)`** -- функция расчета площади для прямоугольника с сторонами $a$, $b$.
  
    *Пример использования:*
  
    `s = area(10, 2) # s = 20`
  
    `s = area(10, 0.2) # s = 2`
  
- **`perimeter(a, b)`** -- функция расчета периметра прямоугольника с сторонами $a$, $b$.
- 
    *Пример использования:*
  
    `p = perimeter(10, 2) # s = 24`
  
    `p = perimeter(10, 10.1) # s = 40.2`

### [square.py](../square.py)
- **`area(a)`** -- функция расчета площади для квадрата с стороной $a$.
  
    *Пример использования:*
  
    `s = area(10) # s = 100`
  
    `s = area(0.5) # s = 0.25`
- **`perimeter(a)`** -- функция расчета периметра квадрата с стороной $a$.
  
    *Пример использования:*
  
    `p = perimeter(10) # s = 40`
  
    `p = perimeter(10.1) # s = 40.4`

### [circle.py](../circle.py)
- **`area(r)`** -- функция расчета площади для круга с радиусом $r$.
  
    *Пример использования:*
  
    `s = area(10) # s = 314.1592653589793`
  
- **`perimeter(r)`** -- функция расчета периметра круга с радиусом $r$.
  
    *Пример использования:*
  
    `p = perimeter(10) # s = 62.83185307179586`

### [triangle.py](../triangle.py)
- **`area(a, h)`** -- функция расчета площади для треугольника с стороной $a$ и высотой $h$ (опущенной к стороне $a$).
- 
    *Пример использования:*
  
    `s = area(5, 3) # s =7.5 `
  
- **`perimeter(r)`** -- функция расчета периметра треугольника с сторонами $a$, $b$, $c$.
  
    *Пример использования:*
  
    `p = perimeter(10, 5, 6) # s = 21`
  
    `p = perimeter(10.1, 5, 6) # s = 21.1`

## История коммитов
- [08d7d3](https://github.com/l3sssia/geometric_lib/commit/08d7d301aefcc34ec90f750a17bd41a3d83ae272) Добавлены новые тесты для круга
- [e6cd3f](https://github.com/l3sssia/geometric_lib/commit/e6cd3f9a04612902c9b1826ac36c4d712fb47fcd) Автотесты Github Actions
- [7e2f08](https://github.com/l3sssia/geometric_lib/commit/7e2f08e106e45aa8a646543c84ac7480f34dc46e) Тесты добавлены в ветку main
- [33618b](https://github.com/l3sssia/geometric_lib/commit/33618be305b24dede28e1c7303921c03d6dbd03c) Lab-2 слита с main
- [ffd110](https://github.com/l3sssia/geometric_lib/commit/ffd110b6d5683327e9095fa8e5820bea13e67bca) Добавлен readme

### Patch 1
- [04c09c](https://github.com/l3sssia/geometric_lib/commit/04c09c8e8a0d2c8d2d349047f2eded7c38369e48) Автотесты Github Actions

### Ветка tests -- добавлены тесты
- [8048f4c](https://github.com/l3sssia/geometric_lib/commit/8048f4c) Исправлены тесты
- [742d1c6](https://github.com/l3sssia/geometric_lib/commit/742d1c6e3607dc5171162930001467c7640e486e) Добавлены тесты

### Ветка lab-2 -- добавлены docstrings для файлов
- [67e6f9](https://github.com/l3sssia/geometric_lib/commit/67e6f9) add description in triangle.py
- [85b72b](https://github.com/l3sssia/geometric_lib/commit/85b72bcd718a9d238ced4bd17435885726865b80) fix description in rectangle.py
- [a2e73f](https://github.com/l3sssia/geometric_lib/commit/a2e73f6c747d672ce472fb00e339eb66f40ef63c) add description in square.py
- [d05a4d](https://github.com/l3sssia/geometric_lib/commit/d05a4d5b9e0c619cc4ea32d586c55a98118bc028) add description in rectangle.py
- [082207](https://github.com/l3sssia/geometric_lib/commit/0822079d2925d73530f9bbd53f5d5a8428fa9877) add description in circle.py

### Добавление вычислений для прямоугольника и треугольника
- [ed5718](https://github.com/l3sssia/geometric_lib/commit/ed5718b4e0f7110e1da649180a36f1b6173f4ddf) fix rectangle.py; add triangle.py
- [01de94](https://github.com/l3sssia/geometric_lib/commit/01de94d9e439ebab3231d2d003ac21f8390e4597) add rectangle.py


  
