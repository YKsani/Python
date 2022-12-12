# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования

import sys
sys.path.append("./Leasson 9")
from telegram_token import telegram_token
import logging
import loger
import calculator
from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          Filters,
                          ConversationHandler)
from telegram import ReplyKeyboardMarkup

TOKEN = telegram_token

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

TYPE, ACTION, GIVE_NUM, RESULT, MENU = range(5)

type_num = None
action = None


def start(update, _):
    user = update.message.from_user
    loger.logger_start(user.id, user.first_name, update.message.text)
    reply_keyboard = [["Начнем"]]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(f"Приветствую, {update.effective_user.first_name}!\n"
                              "Я калькулятор и я могу посчитать, Ваш, пример\n\n"
                              "Попробуем?\n\n"
                              "/start - запустить бот\n"
                              "/stop - остановить бот",
                              reply_markup=markup_key)
    return TYPE


def type_command(update, _):
    global type_num
    user = update.message.from_user
    loger.logger_message(user.id, user.first_name, update.message.text)
    reply_keyboard = [["Рациональные", "Комплексные"]]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(f"Выберите с какими числами будем работать?", reply_markup=markup_key)
    return ACTION


def action_num(update, _):
    global action, type_num
    user = update.message.from_user
    loger.logger_message(user.id, user.first_name, update.message.text)
    type_num = update.message.text
    reply_keyboard = [["+", "-", "*", "/", "**"]]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(f"Выберите действие:\n\n"
                              f"/back - вернуться в предыдущее меню", reply_markup=markup_key)
    return GIVE_NUM


def give_num(update, _):
    global type_num, action
    user = update.message.from_user
    loger.logger_message(user.id, user.first_name, update.message.text)
    action = update.message.text
    if action == "/back":
        reply_keyboard = [["Рациональные", "Комплексные"]]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text("Выберите с какими числами будет работать?", reply_markup=markup_key)
        return ACTION
    else:
        if type_num == "Рациональные":
            update.message.reply_text("Введите 2 числа через пробел:")
        elif type_num == "Комплексные":
            update.message.reply_text("Введите 4 числа через пробел:")
    return RESULT


def res(update, _):
    reply_keyboard = [["Продолжить"], ["Завершить"]]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    global type_num, action
    user = update.message.from_user
    loger.logger_message(user.id, user.first_name, update.message.text)
    num = update.message.text
    d = num.replace(".", "").replace(" ", "")
    numbers = num.split()
    if d.isdigit() and len(numbers) >= 2:
        if type_num == "Рациональные" and len(numbers) == 2:
            if numbers[1] == "0" and action == "/":
                update.message.reply_text("Ошибка: деление на ноль\n"
                                          "Введите числа через пробел:")
                loger.logger_error(user.id, user.first_name, "Попытка деления на ноль")
                return RESULT
            else:
                res1 = calculator.calculate_rational(numbers, action)
                update.message.reply_text(f"Результат:\n"
                                          f"{numbers[0]} {action} {numbers[1]} = {res1}\n\n"
                                          "Выберите действие:", reply_markup=markup_key)
                loger.logger_result(user.id, user.first_name, res1)
                return MENU
        elif type_num == "Комплексные" and len(numbers) == 4:
            if numbers[2] == "0" and numbers[3] == "0" and action == "/":
                update.message.reply_text("Ошибка: деление на ноль\n"
                                          "Введите числа через пробел:")
                loger.logger_error(user.id, user.first_name, "Попытка деления на ноль")
                return RESULT
            else:
                res1 = calculator.calculate_complex(numbers, action)
                a = complex(float(numbers[0]), float(numbers[1]))
                b = complex(float(numbers[2]), float(numbers[3]))
                update.message.reply_text(f"Результат:\n"
                                          f"{a} {action} {b} = {res1}\n\n"
                                          "Выберите действие:", reply_markup=markup_key)
                loger.logger_result(user.id, user.first_name, res1)
                return MENU
        else:
            if type_num == "Рациональные":
                update.message.reply_text("Ошибка: некорректное количество чисел\n"
                                          "Введите 2 числа через пробел:")
            elif type_num == "Комплексные":
                update.message.reply_text("Ошибка: некорректное количество чисел\n"
                                          "Введите 4 числа через пробел:")
            loger.logger_error(user.id, user.first_name, "Некорректное количество чисел при вводе")
            return RESULT
    else:
        if type_num == "Рациональные":
            update.message.reply_text("Ошибка: некорректное значение\n"
                                      "Введите 2 числа через пробел:")
        elif type_num == "Комплексные":
            update.message.reply_text("Ошибка: некорректное значение\n"
                                      "Введите 4 числа через пробел:")
        loger.logger_error(user.id, user.first_name, "Некорректное значение при вводе чисел")
        return RESULT


def menu(update, _):
    global action
    user = update.message.from_user
    loger.logger_message(user.id, user.first_name, update.message.text)
    action = update.message.text
    reply_keyboard = [["Рациональные", "Комплексные"]]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    if action == "Продолжить":
        update.message.reply_text(f"Продолжим\n"
                                  f"Выберите с какими числами будем работать?", reply_markup=markup_key)
        return ACTION
    elif action == "Завершить":
        loger.logger_stop(user.id, user.first_name, update.message.text)
        update.message.reply_text("До свидания!\n\n"
                                  "/start - запустить бот")
        return ConversationHandler.END


def stop(update, _):
    user = update.message.from_user
    loger.logger_stop(user.id, user.first_name, update.message.text)
    update.message.reply_text("До свидания!\n\n"
                              "/start - запустить бот")
    return ConversationHandler.END


if __name__ == "__main__":
    conv_handler = ConversationHandler(entry_points=[CommandHandler("start", start)],
                                       states={TYPE: [MessageHandler(Filters.regex("Начнем"), type_command)],
                                               ACTION: [MessageHandler(Filters.text, action_num)],
                                               GIVE_NUM: [MessageHandler(Filters.text, give_num)],
                                               RESULT: [MessageHandler(Filters.text, res)],
                                               MENU: [MessageHandler(Filters.text, menu)]},
                                       fallbacks=[CommandHandler("stop", stop)])

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
