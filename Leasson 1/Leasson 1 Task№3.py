# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
import sys


def input_value_x():
    try:
        x = int(input('Введите значение х: '))
        if x == 0:
            print('Вы ввели некорректное значение, повторите.')
        return x
    except ValueError:
        print('Вы ввели некорректное значение')
        sys.exit()


def input_value_y():
    try:
        y = int(input('Введите значение y: '))
        if y == 0:
            print('Вы ввели некорректное значение, повторите.')
        return y
    except TypeError:
        print('Вы ввели некорректное значение')
        sys.exit()


def quarter_search(x, y):
    result = 0
    if x > 0 and y > 0:
        result = 1
    elif x > 0 and y < 0:
        result = 4
    elif x < 0 and y > 0:
        result = 2
    elif x < 0 and y < 0:
        result = 3
    return result


quarter = quarter_search(input_value_x(), input_value_y())
print(f'Для введенных значений четверть = {quarter}')
