# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers_list = [1.1, 1.2, 3.1, 5, 10.01]

maxi = numbers_list[0] - int(numbers_list[0])
mini = numbers_list[0] - int(numbers_list[0])
for num in numbers_list:
    if num - int(num) != 0:
        if maxi < num - int(num):
            maxi = num - int(num)
        elif mini > num - int(num):
            mini = num - int(num)
print(format(maxi - mini, ".2f"))
