# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

import sys


def input_value_quarter():
    try:
        quarter = int(input('Введите значение четверти: '))
        return quarter
    except ValueError:
        print('Вы ввели некорректное значение')
        sys.exit()

def print_all_value_in_quarter(quarter):
    if quarter == 1:
        print(f"x ∈ (0; +∞) y ∈ (0; +∞)")
    elif quarter == 2:
        print(f"x ∈ (-∞; 0) y ∈ (0; +∞)")
    elif quarter == 3:
        print(f"x ∈ (-∞; 0) y ∈ (-∞; 0)")
    elif quarter == 4:
        print(f"x ∈ (0; +∞) y ∈ (-∞; 0)")

quarter = input_value_quarter()
print_all_value_in_quarter(quarter)
