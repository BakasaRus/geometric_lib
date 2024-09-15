def checkValues(a, b):
    if (a < 0):
        raise ValueError("Given negative value for rectangle side a: ", a)
    if (b < 0):
        raise ValueError("Given negative value for rectangle side b: ", b)

def area(a, b):
    '''
    Возвращает площадь прямоугольника в зависимости от длин его сторон

        Параметры:
            a (int/float): длина первой стороны прямоугольника
            b (int/float): длина второй стороны прямоугольника

        Возвращаемое значение:
            area (int/float): площадь прямоугольника с сторонами a и b
    '''
    checkValues(a, b)
    return a * b


def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника в зависимости от длин его сторон

        Параметры:
            a (int/float): длина первой стороны прямоугольника
            b (int/float): длина второй стороны прямоугольника

        Возвращаемое значение:
            perimeter (int/float): периметр прямоугольника с сторонами a и b
    '''
    checkValues(a, b)
    return (a + b) * 2
