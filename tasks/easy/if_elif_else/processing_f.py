"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Дана строка. В зависимости от того, сколько встречается в строке буква f,
выполнить следующие действия:
    - 0 раз: буквы нижнего регистра заменить на верхний, верхнего на нижний
    - 1 раз: вывести ее индекс
    - 2 раза: вывести индекс последнего вхождения
    - больше 2 раз: вернуть исходную строку задом-наперед

ПРИМЕРЫ
--------------------------------------------------------------------------------
- 'Hello World' -> 'hELLO wORLD'
- 'hi-fi acoustic' -> 3
- 'fast forward' -> 5
- 'finish false fox' -> 'xof eslaf hsinif'
"""
from typing import Union


def processing_f(str_with_f: str) -> Union[int, str]:
    """Выполняет действия в зависимости от количества вхождений f

    :param str_with_f: строка для работы
    :type str_with_f: str

    :return: строку или индекс
    :rtype: str
    """
    num = str_with_f.count('f')
    if num == 0:
        result = str_with_f.swapcase()
    elif num == 1:
        result = str_with_f.find('f')
    elif num == 2:
        result = str_with_f.rfind('f')
    else:
        result = str_with_f[::-1]
    return result


if __name__ == '__main__':
    string = input('Введите строку для работы: ')
    print(f"Результат: {processing_f(string)}")
