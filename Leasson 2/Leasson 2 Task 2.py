# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Input format
# Одно целое число
# Output format
# Последовательность целых чисел через пробел

n=int(input())
for num in range (1,n+1):
    prod=1
    for n in range (1,num+1):
        prod*=n
    print(prod)