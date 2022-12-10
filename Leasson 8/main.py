# Доделать решение задачи: Задача:
# Создать информационную систему, позволяющую работать с сотрудниками некой компании
# \ студентами вуза \ учениками школы


import data_handling as dh
import time


def input_action():
    command = ''
    while command != 'q':
        print("\nМеню:\n\
        1 - Показать справочник\n\
        2 - Добавить контакт\n\
        3 - Редактировать контакт\n\
        4 - Удалить контакт\n\
        5 - Поиск контакта\n\
        6 - Экспорт данных\n\
        q - Выход\n")
        command = str.lower(input('Выберете действие: '))
        if command == "1":
            dh.print_data()
        elif command == "2":
            dh.import_record(dh.input_data())
        elif command == "3":
            dh.edit_data()
        elif command == "4":
            dh.remove_data()
        elif command == "5":
            dh.print_record()
        elif command == "6":
            dh.export_data()
        time.sleep(2)
    exit()


program_execution = True
while program_execution:
    program_execution = input_action()
