head_table = ["Id", "Фамилия", "Имя", "Отчество", "Телефон", "Комментарий"]


def input_data():
    data = output_data()
    id = int(data[-1][0]) + 1
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic_name = input("Введите отчество: ")
    phone_number = input("Введите телефон: ")
    comment = input("Введите комментарий: ")
    return [str(id), last_name, first_name, patronymic_name, phone_number, comment]


def import_record(record):
    with open("phonebook.csv", "a", encoding="utf-8") as file:
        file.write(",".join(record))
        file.write(f"\n")


def import_data(data):
    with open("phonebook.csv", "w", encoding="utf-8") as file:
        file.write(",".join(head_table))
        file.write("\n")
        for rec in data:
            file.write(",".join(rec))
            file.write("\n")


def export_data():
    try:
        data = output_data()
        file_path = "export files" + "/"
        filename = input("\nВведите имя файла:")
        print("Выберите тип файла:\n\
    1 - .csv (таблица) *по умолчанию\n\
    2 - .txt (записная книжка)")
        chs = input()
        if chs == "1":
            file_extension = ".csv"
        elif chs == "2":
            file_extension = ".txt"
        else:
            file_extension = ".csv"
        with open(file_path + filename + file_extension, "w", encoding="utf-8") as file:
            if file_extension == ".csv":
                file.write(",".join(head_table))
                file.write("\n")
                for rec in data:
                    file.write(",".join(rec))
                    file.write("\n")
            elif file_extension == ".txt":
                for rec in data:
                    c = 0
                    for item in rec:
                        file.write(f"{head_table[c]}: {item}\n")
                        c += 1
                    file.write("\n")
    except ValueError:
        print("Ошибка: Не корректное имя файла")


def output_data():
    data = []
    with open("phonebook.csv", "r", encoding="utf-8") as file:
        for line in file:
            s = line.strip().split(",")
            if s != head_table:
                data.append(s)
    return data


def search_data(data, value):
    if len(data) > 0:
        temp_search = []
        is_search = False
        for rec in data:
            for item in rec:
                if str.lower(item) == str.lower(value):
                    is_search = True
            if is_search:
                temp_search.append(rec)
            is_search = False
        return temp_search
    else:
        return None


def remove_data():
    id_remove = int(input("Введите Id записи, которую хотите удалить: "))
    data = output_data()
    del data[id_remove - 1]
    i = 0
    for rec in data:
        rec[0] = str(i + 1)
        i += 1
    import_data(data)
    print(f"\nЗапись с Id = {id_remove} удалена")


def print_data():
    data = output_data()
    if len(data) > 0:
        print()
        print(head_table[0].center(5), head_table[1].center(15), head_table[2].center(15), head_table[3].center(15),
              head_table[4].center(20), head_table[5].center(20))
        print("-" * 95)
        for rec in data:
            print(rec[0].center(5), rec[1].center(15), rec[2].center(15), rec[3].center(15), rec[4].center(20),
                  rec[5].center(20))
    else:
        print("\nСправочник пуст")


def print_record():
    value = input("Введите данные для поиска: ")
    data = search_data(output_data(), value)
    if len(data) > 0:
        print()
        print(head_table[0].center(5), head_table[1].center(15), head_table[2].center(15), head_table[3].center(15),
              head_table[4].center(20), head_table[5].center(20))
        print("-" * 95)
        for rec in data:
            print(rec[0].center(5), rec[1].center(15), rec[2].center(15), rec[3].center(15), rec[4].center(20),
                  rec[5].center(20))
    else:
        print("\nЗапись не найдена")


def edit_data():
    id_edit = int(input("Введите Id записи, которую хотите отредактировать: "))
    data = output_data()
    print()
    print(head_table[0].center(5), head_table[1].center(15), head_table[2].center(15), head_table[3].center(15),
          head_table[4].center(20), head_table[5].center(20))
    print("-" * 95)
    print(data[id_edit - 1][0].center(5), data[id_edit - 1][1].center(15), data[id_edit - 1][2].center(15),
          data[id_edit - 1][3].center(15), data[id_edit - 1][4].center(20), data[id_edit - 1][5].center(20))
    function_execution = True
    while function_execution:
        print(f"\nВыберите какую колонку хотите отредактировать:\n\
    1 - {head_table[1]}\n\
    2 - {head_table[2]}\n\
    3 - {head_table[3]}\n\
    4 - {head_table[4]}\n\
    5 - {head_table[5]}\n\
    save - Сохранить изменения\n\
    cancel - Отменить изменения\n")
        action = str.lower(input("Выберите действие: "))
        if action in ["1", "2", "3", "4", "5"]:
            action = int(action)
            data[id_edit - 1][action] = input(f"Введите новое значение колонки {head_table[action]}: ")
            print("Значение колонки изменено")
        elif action == "save":
            import_data(data)
            function_execution = False
        elif action == "cancel":
            function_execution = False
