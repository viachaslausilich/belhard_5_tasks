"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Необходимо отредактировать функцию square_or_rectangle, которая принимает
длины двух сторон, так, чтобы она возвращала площадь квадрата, если
фигура квадрат, либо периметр, если фигура прямоугольник

ПРИМЕРЫ
--------------------------------------------------------------------------------
square_or_rectangle(6, 10) -> 32
square_or_rectangle(4, 4) -> 16
"""


def square_or_rectangle(side1: int, side2: int) -> int:
    if side1 == side2:
        result = side1 * side2
    else:
        result = (side1 + side2) * 2
    return result


if __name__ == '__main__':
    side1_val = int(input('Введите длину первой стороны: '))
    side2_val = int(input('Введите длину второй стороны: '))
    print(f'Результат: {square_or_rectangle(side1_val, side2_val)}')
