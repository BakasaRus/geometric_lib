# Общее описание решения
4 файла:
=
- triangle.py	треугольник(площадь и периметр)
- square.py	квадрат(площадь и периметр)
- rectangle.py	прямоугольник(площадь и периметр)
- circle.py	круг(площадь и длинна окружности)
# Описание каждой функции с примерами вызова
## triangle.py
### area
    Принимает a(сторона треугольника),h (высота треугольника)
    Возвращает a*h/2 (площадь треугольника)
Пример:
```python
    def area(a, h):
    return a * 2 /h 
```
### perimeter
    Принимает a,b,c (стороны треугольника)
    Возвращает a+b+c (периметр треугольника)
Пример:
```python
    def perimeter(a, b, c):
    return a + b + c
```
## square.py
### area
    Принимает a (сторону квадрата)
    Возвращает a*a (площадь квадрата)
Пример:
```python
def area(a):
    return a * a
```
### perimeter
    Принимает a (сторону квадрата)
    Возвращает a*4 (периметр квадрата)
Пример:
```python
def perimeter(a):
    return 4 * a
```
## rectangle.py
### area
    Принимает a,b (стороны прямоугольника)
    Возвращает a*b (площадь прямоугольника)
Пример:
```python
def area(a, b):
    return a * b
```
### perimeter
    Принимает a,b (стороны прямоугольника)
    Возвращает 2*(a+b) (периметр прямоугольника)
Пример:
```python
def perimeter(a, b):
    return 2*(a + b)
```
## circle.py
### area
    Принимает r (радиус круга)
    Возвращает r*r*pi (площадь круга)
Пример:
```python
import math
def area(r):
    return math.pi * r * r
```
### perimeter
    Принимает r (радиус окружности)
    Возвращает 2*r*pi (длинна окружности)
Пример:
```python
import math
def perimeter(r):
    return 2 * math.pi * r
```
# История изменения проекта с хешами комитов (кроме последней записи)



| Коммит                                                       | Комментарий                             |
|--------------------------------------------------------------|-----------------------------------------|
|commit 4d4d9e4f7a265ebb8efe8b04f48bdb323a772702 (HEAD -> main, origin/main, origin/HEAD)<br/>Author: Daniil Dvinin <dvininden@gmail.com><br/>Date:   Thu Sep 28 19:23:45 2023 +0300|feat: added description in docs|
|commit 2908219509263bdf3e8cd6fbfb2e206e0de89e16 (HEAD -> main)<br/>Author: Daniil Dvinin <dvininden@gmail.com><br/>Date:   Thu Sep 28 18:14:34 2023 +0300| feat: added description to  triangle.py |              |-------------|
|commit c4d9dfbdb9d5d90df27f05c03517e59b9754ba53<br/> Author: Daniil Dvinin <dvininden@gmail.com><br/>Date:   Thu Sep 28 18:08:31 2023 +0300| feat: added description to square.py    |
|commit 1c09a3b735c19f67650e52ac28bbaa23f0aeb4ac<br/>Author: Daniil Dvinin <dvininden@gmail.com><br/>Date:   Thu Sep 28 17:58:14 2023 +0300| feat: added description to rectangle.py |
|commit 21a5f89b093cc7d44dfc24f4809fe4fd4b09ae34<br/>Author: Daniil Dvinin <dvininden@gmail.com><br/>Date:   Thu Sep 28 17:52:10 2023 +0300| feat: added description to circle.py    |
|commit 2908219509263bdf3e8cd6fbfb2e206e0de89e16 (HEAD -> main)<br/>Author: Daniil Dvinin <dvininden@gmail.com><br/>Date:   Thu Sep 28 18:14:34 2023 +0300| feat: added description to  triangle.py |
|commit c4d9dfbdb9d5d90df27f05c03517e59b9754ba53<br/>Author: Daniil Dvinin <dvininden@gmail.com><br/>Date:   Thu Sep 28 18:08:31 2023 +0300| feat: added description to square.py    |
|commit 1c09a3b735c19f67650e52ac28bbaa23f0aeb4ac<br/>Author: Daniil Dvinin <dvininden@gmail.com><br/>Date:   Thu Sep 28 17:58:14 2023 +0300|feat: added description to rectangle.py|
|commit 21a5f89b093cc7d44dfc24f4809fe4fd4b09ae34<br/>Author: Daniil Dvinin <dvininden@gmail.com><br/>Date:   Thu Sep 28 17:52:10 2023 +0300|feat: added description to circle.py|
|commit ceaf2e50119d82ff77f469f81a4cdc2e9d9bc192 (origin/main, origin/HEAD, description)<br/>Author: Daniil Dvinin <dvininden@gmail.com><br/>Date:   Sat Sep 9 12:10:14 2023 +0300|feat: Add triangle.py  fix: fix perimeter rectangle.py|
|commit e757aa8ee9a7bfa32d047444f19c87eb2e7e1292<br/>Author: Daniil Dvinin <dvininden@gmail.com><br/>Date:   Sat Sep 9 11:53:18 2023 +0300|feat:  rectangle.py|
|commit d078c8d9ee6155f3cb0e577d28d337b791de28e2<br/>Author: smartiqa <info@smartiqa.ru><br/>Date:   Thu Mar 4 14:55:29 2021 +0300|L-03: Docs added|
|commit 8ba9aeb3cea847b63a91ac378a2a6db758682460<br/>Author: smartiqa <info@smartiqa.ru><br/>Date:   Thu Mar 4 14:54:08 2021 +0300|L-03: Circle and square added|
#Котик
![img.png](img.png)