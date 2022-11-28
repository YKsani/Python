# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def input_dat(name):
    try:
        x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
        while x < 1 or x > 28:
            x = int(input(f"{name}, введите корректное количество конфет: "))
        return x
    except(ValueError, UnboundLocalError):
        print("Вы ввели некорректное значение")
        exit()

def p_print(name, candies, counter, value):
    print(f"{name} сделал свой ход и взял {candies} конфет, всего их у него {counter}. Осталось на столе {value} конфет. \n")


def bot_calc(value):
    candies = randint(1, 29)
    while value - candies <= 28 and value > 29:
        candies = randint(1, 29)
    return candies

player_one = input("Введите имя первого игрока: ")
player_two = "Bot"
value = 2021
flag = randint(0,2)
if flag:
    print(f"{player_one} - Вам повезло, ходите первым!")
else:
    print(f"{player_two} ходит первым.")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        candies = input_dat(player_one)
        counter1 += candies
        value -= candies
        flag = False
        p_print(player_one, candies, counter1, value)
    else:
        candies = bot_calc(value)
        counter2 += candies
        value -= candies
        flag = True
        p_print(player_two, candies, counter2, value)

if flag:
    print(f"Выиграл {player_one}")
else:
    print(f"Выиграл {player_two}")
