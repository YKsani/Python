# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number_fibonacci = int(input('Введите число: '))

def get_fibonacci(number_fibonacci):
    fibo_nums = []
    fib1, fib2 = 1, 1
    for i in range(number_fibonacci):
        fibo_nums.append(fib1)
        fib1, fib2 = fib2, fib1 + fib2
    fib1, fib2 = 0, 1
    for i in range(number_fibonacci + 1):
        fibo_nums.insert(0, fib1)
        fib1, fib2 = fib2, fib1 - fib2
    return fibo_nums

print(get_fibonacci(number_fibonacci))

