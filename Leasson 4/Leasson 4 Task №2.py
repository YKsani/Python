# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def calculate_values(n):
    i = 2
    list_simple = []
    while i <= n:
        if n % i == 0:
            list_simple.append(i)
            n //= i
            i = 2
        else:
            i += 1
    return list_simple


print(", ".join(map(str, calculate_values(int(input('Введите натуральное число: '))))))
