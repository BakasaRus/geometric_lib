# Geometric Lib
## Поддерживает операции над следующими фигурами:
- круг - Circle.py
- прямоугольник - Rectangle.py
- квадрта - Square.py
- треугольник - Triangle.py

### Circle.py
- `def area(r)` принимает радиус круга и возвращает площадь круга - **S = πR<sup>2</sup>**
> Пример - area(2) = 12.56637
- `def perimeter(r)` принимает радиус круга и возвращает периметр круга - **P = 2πR**
> Пример - petimeter(2.5) = 7.85398

### 2) Rectangle.py
- `def area(a, b)` принимает длины сторон прямоугольника и возвращает площадь прямоугольника - **S = a * b**
> Пример - area(2, 6) = 12
- `def perimeter(a, b)` принимает длины сторон пямоугольника и возвращает периметр прямоугольника - **P = 2 * (a + b)**
> Пример - perimeter(3, 1) = 8
### 3) Square.py
- `def area(a)` принимает длину стороны квадрата и возвращает площадь квадрата - **S = a<sup>2</sup>**
> Пример - area(1.2) = 1.44
- `def perimeter(a)` принимает длину стороны квадрата и возвращает периметр квадрата - **P = 4 * a**
> Пример - perimeter(2) = 8

### 4) Triangle.py
- `def area(a, h)` принимает длину стороны и высоты треугольник и возвращает площадь треугольника - **S = a * (h / 2)**
> Пример - area(2, 3) = 3
- `def perimeter(a, b, c)` принимает длины сторон треугольника и возвращает периметр треугольника - **P = a + b + c**
> Пример - perimeter(1.1, 1.2, 2) = 4.3

## История коммитов:
* 12c4200 (HEAD -> main) [fix]: fixed rectangle.py
* af89b7d [feat]: added triangle.py
* 4e495ff [feat]: added rectangle.py
* d078c8d (origin/main, origin/HEAD) L-03: Docs added
* 8ba9aeb L-03: Circle and square added
