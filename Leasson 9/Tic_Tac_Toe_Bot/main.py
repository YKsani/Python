# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

import sys
sys.path.append("./Leasson 9")
from telegram_token import telegram_token
import random
from aiogram import Bot, Dispatcher, executor, types


TOKEN = telegram_token

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

board = list(range(1, 10))
counter = 0


def print_board():
    return f"| {board[0]} | {board[1]} | {board[2]} |\n" \
           f"| {board[3]} | {board[4]} | {board[5]} |\n" \
           f"| {board[6]} | {board[7]} | {board[8]} |"


def new_board():
    global board, counter
    board = list(range(1, 10))
    counter = 0


def check_winner(board):
    winning_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in winning_combo:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return


def winning_move(b1, b2, b3, player):
    if b1 == player and b2 == player and type(b3) == int:
        return b3
    if b1 == player and type(b2) == int and b3 == player:
        return b2
    if type(b1) == int and b2 == player and b3 == player:
        return b1
    return -1


def computer_move(player, board):
    winning_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in winning_combo:
        win_move = winning_move(board[i[0]], board[i[1]], board[i[2]], player)
        if win_move >= 0:
            board[win_move - 1] = player
            return
    for i in winning_combo:
        win_move = winning_move(board[i[0]], board[i[1]], board[i[2]], "X")
        if win_move >= 0:
            board[win_move - 1] = player
            return
    valid = False
    while not valid:
        rand_move = random.randint(1, 9)
        if (str(board[rand_move - 1]) not in "XO"):
            board[rand_move - 1] = player
            valid = True


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    new_board()
    await bot.send_message(user_id, f"Привет {user_name}\n"
                                    "Давай поиграем в \"Крестики-нолики\"\n"
                                    f"{print_board()}"
                                    f"\nТвой ход:")


@dp.message_handler()
async def msg_handler(message: types.Message):
    global board, counter
    user_id = message.from_user.id
    valid = True
    try:
        move = int(message.text)
    except ValueError:
        valid = False
        await bot.send_message(user_id, "Ошибка: Некорректное значение!")
    if move >= 1 and move <= 9:
        if (str(board[move - 1]) not in "XO"):
            board[move - 1] = "X"
            counter += 1
        else:
            valid = False
            await bot.send_message(user_id, "Эта клеточка уже занята")
    else:
        valid = False
        await bot.send_message(user_id, "Ошибка: Введите число от 1 до 9.")

    if valid:
        await bot.send_message(user_id, f"{print_board()}")
        tmp = check_winner(board)
        if tmp:
            new_board()
            await bot.send_message(user_id, f"{tmp} Выиграл!\n"
                                            f"Давай сыграем ещё раз\n"
                                            f"{print_board()}")
        elif counter >= 9:
            new_board()
            await bot.send_message(user_id, f"Ничья!\n"
                                            f"Давай сыграем ещё раз\n"
                                            f"{print_board()}")
        else:
            computer_move("O", board)
            counter += 1
            await bot.send_message(user_id, "Ход компьютера:\n"
                                            f"{print_board()}")
        tmp = check_winner(board)
        if tmp:
            new_board()
            await bot.send_message(user_id, f"{tmp} Выиграл!\n"
                                            f"Давай сыграем ещё раз\n"
                                            f"{print_board()}")
        elif counter >= 9:
            new_board()
            await bot.send_message(user_id, f"Ничья!\n"
                                            f"Давай сыграем ещё раз\n"
                                            f"{print_board()}")


if __name__ == "__main__":
    print("Server is started")
    executor.start_polling(dp)
    print("Server is stopped")
