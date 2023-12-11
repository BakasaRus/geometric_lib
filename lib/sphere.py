import math

def area(r):
    """
        Возвращает площадь поверхности сферы с заданным радиусом.

            Параметры:
                    r (float / int): радиус сферы
            Возвращаемое значение:
                    area (float): поверхности сферы с радиусом r
    """
    if r <= 0:
        raise ValueError
    return 4.0 * r**2 * math.pi

def volume(r):
    """
        Возвращает объем сферы с заданным радиусом.

            Параметры:
                    r (float / int): радиус сферы
            Возвращаемое значение:
                    volume (float): объем сферы с радиусом r
    """
    if r <= 0:
        raise ValueError
    return area(r) * r / 3.0
