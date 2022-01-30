"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
пользователь вводит 3 строки:
    - строка для проверки (check_str)
    - искомая строка (search_str)
    - заменяемая строка (replace_str)

если в строке для проверки содержится искомая строка - заменить ее на
заменяемую строку и вернуть результат, если не содержатся, то вернуть "Ошибка!"

ПРИМЕРЫ
--------------------------------------------------------------------------------
- ('как у тебя дела', 'у тебя', 'твои') -> 'Как твои дела'
- ('что делаешь', 'ты', 'мы') -> 'Ошибка!'
"""


def replacer(check_str: str, search_str: str, replace_str: str) -> str:
    """Если search_str есть в check_str, то заменяет на replace_str,
    если нет, то возвращает "Ошибка!"

    :param check_str: строка для проверки
    :type check_str: str

    :param search_str: искомая строка
    :type search_str: str

    :param replace_str: строка для замены
    :type replace_str: str

    :return: измененная строка для проверки или строка "Ошибка!"
    :rtype: str
    """
    if check_str.find(search_str) >= 0:
        some = check_str.replace(search_str, replace_str)
        result = some.capitalize()
    else:
        result = "Ошибка!"
    return result


if __name__ == '__main__':
    c_string = input('Введите строку для проверки: ')
    s_string = input('Введите строку для поиска: ')
    r_string = input('Введите строку для замены: ')
    print(f'Результат: {replacer(c_string, s_string, r_string)}')
