# Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.


import data_handling as dh


def input_action():
    prog_exec = True
    print("\nМеню:\n\
    1 - Импорт данных\n\
    2 - Экспорт данных\n\
    3 - Показать справочник\n\
    4 - Выход\n")
    choose = input("Выберите действие: ")
    if choose == "1":
        dh.import_data(dh.input_data())
    elif choose == "2":
        try:
            data = dh.output_data()
            filename = input("\nВведите имя файла:")
            print("Выберите формат файла: :\n\
            1 - .csv (по умолчанию)\n\
            2 - .txt")
            chs = input()
            if chs == "1":
                file_extension = ".csv"
            elif chs == "2":
                file_extension = ".txt"
            else:
                file_extension = ".csv"
            file_path = "export files" + "/"
            dh.export_data(data, file_path + filename + file_extension)
        except ValueError:
            print("Ошибка: Не корректное имя файла")
    elif choose == "3":
        data = dh.output_data()
        dh.print_data(data)
    elif choose == "4":
        prog_exec = False
    return prog_exec


program_execution = True
while program_execution:
    program_execution = input_action()
