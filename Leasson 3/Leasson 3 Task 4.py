# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

numbers = int(input('Введите число: '))
numbers_list = []
while numbers != 0:
    if numbers % 2 == 0:
        numbers_list.append(0)
    else:
        numbers_list.append(1)
    numbers //= 2
print("".join(map(str,numbers_list)))