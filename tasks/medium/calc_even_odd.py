"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать программу, которая будет выводить количество четных и нечетных значений
в списке из целых чисел

even - четные
odd - нечетные
"""


def calc_even_odd(array: list) -> tuple:
    leven = []
    lodd = []
    for i in array:
        if i % 2 == 0:
            leven.append(i)
        else:
            lodd.append(i)
    even = len(leven)
    odd = len(lodd)
    return even, odd


if __name__ == '__main__':
    assert calc_even_odd([2, 1, 5, 4, 7]) == (2, 3)
    print('Решено!')
