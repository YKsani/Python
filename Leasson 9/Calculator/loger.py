from datetime import datetime as dt

l_separator = "=========="
l_1 = "Пользователь начал работу"
l_2 = "Сообщение от пользователя"
l_3 = "Результат вычислений"
l_4 = "Ошибка"
l_5 = "Пользователь завершил работу"


def logger_start(l_user_id, l_user_name, l_message):
    time = dt.now().strftime("%D (%H/%M)")
    with open("log.csv", "a", encoding="utf-8") as file:
        file.write(f"{l_separator}:{l_separator}:{l_separator}:{l_1}:{l_separator}\n")
        file.write(f"{time}:{l_user_id}:{l_user_name}:{l_2}:{l_message}\n")


def logger_message(l_user_id, l_user_name, l_message):
    time = dt.now().strftime("%D (%H/%M)")
    with open("log.csv", "a", encoding="utf-8") as file:
        file.write(f"{time}:{l_user_id}:{l_user_name}:{l_2}:{l_message}\n")


def logger_result(l_user_id, l_user_name, l_result):
    time = dt.now().strftime("%D (%H/%M)")
    with open("log.csv", "a", encoding="utf-8") as file:
        file.write(f"{time}:{l_user_id}:{l_user_name}:{l_3}:{l_result}\n")


def logger_error(l_user_id, l_user_name, l_error):
    time = dt.now().strftime("%D (%H/%M)")
    with open("log.csv", "a", encoding="utf-8") as file:
        file.write(f"{time}:{l_user_id}:{l_user_name}:{l_4}:{l_error}\n")


def logger_stop(l_user_id, l_user_name, l_message):
    time = dt.now().strftime("%D (%H/%M)")
    with open("log.csv", "a", encoding="utf-8") as file:
        file.write(f"{time}:{l_user_id}:{l_user_name}:{l_2}:{l_message}\n")
        file.write(f"{l_separator}:{l_separator}:{l_separator}:{l_5}:{l_separator}\n")
