# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers_list = [2, 3, 4, 5, 6]
multiplication_list = []
number_from_end = len(numbers_list) - 1
for i in range(1):
    while i < len(numbers_list) / 2:
        a = numbers_list[i] * numbers_list[number_from_end]
        multiplication_list.append(a)
        i += 1
        number_from_end -= 1
print(multiplication_list)
