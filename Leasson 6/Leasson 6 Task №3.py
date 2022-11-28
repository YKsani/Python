# Формат: Объясняет преподаватель
#
# Задача: предложить улучшения кода для уже решённых задач:
#
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


numbers = int(input("Введите число N: "))
multiplication_numbers = lambda x: 1 if x == 0 else x * multiplication_numbers(x - 1)
print(f"Произведение чисел от 1 до {numbers} =  {[*map(multiplication_numbers, [i for i in range(1, numbers + 1)])]}")