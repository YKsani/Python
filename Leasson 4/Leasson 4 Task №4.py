# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите натуральную степень: '))
numbers_list = [random.randint(0, 100) for i in range(k + 1)]


def calculate_values(lst):
    s: str = ""
    for i in range(len(lst)):
        if i < len(lst) - 2:
            if lst[i] > 1:
                s += f"{lst[i]}x^{len(lst) - i - 1}"
            elif lst[i] == 1:
                s += f"x^{len(lst) - i - 1}"
            if lst[i + 1] != 0:
                s += " + "
        elif i == len(lst) - 2:
            if lst[i] > 1:
                s += f"{lst[i]}x"
            elif lst[i] == 1:
                s += f"x"
            if lst[i + 1] != 0:
                s += " + "
        elif i == len(lst) - 1:
            if lst[i] >= 1:
                s += f"{lst[i]}"
    s += " = 0"
    print(s)
    return s


with open("file_task№4.txt", "w", encoding="utf-8") as file:
    file.write(calculate_values(numbers_list))
