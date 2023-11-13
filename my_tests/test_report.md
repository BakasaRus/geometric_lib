# Tests report

## Цели и задачи тестирования

- Целью тестирования продукта является сравнение ожидаемых и реальных результатов выполнения программы при различных
  входных данных
- Задача - выявление неккорекного поведения в ситуациях не учтённых при написании исходного кода

## Описание тестируемого продукта

Тестируемый продукт библиотека с математическими функциями позволяющая высчитывать площадь и периметр поддерживаемых
геометрических фигур а именно круга прямоугольника квадрата и треугольника

## Область тестирования

- circle
    - area(r)
      takes the radius of the circle, returns area of the circle - $S = \pi R^2$
    - perimeter(r)
      takes the radius of the circle, returns perimeter of the circle - $P = 2\pi R$
- rectangle
    - area(a, b)
      takes the lengths of the two sides of rectangle, returns area of the rectangle - $S = ab$
    - perimeter(a, b)
      takes the lengths of the two sides of rectangle, returns perimeter of the rectangle - $P = 2a + 2b$
- square
    - area(a, b)
      takes the lengths of the two sides of rectangle, returns area of the rectangle - $S = a^2$
    - perimeter(a, b)
      takes the lengths of the two sides of rectangle, returns perimeter of the rectangle - $P = 4a$
- triangle
    - area(a, h)
      Takes the length of the side of triangle and the length of height, returns area of the triangle - $S = \frac{1}{2}
      ah$
    - perimeter(a, b, c)
      Takes the lengths of the three sides of triangle, returns perimeter of the triangle - $P = a + b + c$

## Стратегия тестирования

### Функциональное модульное тестирование функций библиотеки

- Определяем входные данные, которые будут поданы в программу
- На основе них высчитываем ожидаемый результат
- Запускаем программу и сравниваем ожидаемый результат с реальным

## Критерии приёмки

- При вводе корректных данных, функция возвращает ожидаемый результат
- При вводе некорректных данных, функция возвращает ошибку

## Результаты

### Ожидаемые результаты

Некоректная обработка отрицательных значений (функция не будет возвращать ошибки)
Обработка значений несуществующих фигур

### Метрики

| Module | Passed | Failed |
|--------|--------|--------|
| Circle    | 6      | 1      |
| Rectangle | 6      | 1      |
| Square    | 6      | 1      |
| Triangle  | 5      | 3      |

Провалено 6 тестов

## Итог

Причины неправильных ответов:

- функции неправильно обрабатывают отрицательные значения
- некоторые функции могут выводить целые числа в виде мантиссы
- функции могут обрабатывать значения фигур, которыг в реальности не может существовать


