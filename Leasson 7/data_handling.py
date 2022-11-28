def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic_name = input("Введите отчество: ")
    phone_number = input("Введите телефон: ")
    comment = input("Введите комментарий: ")
    return [last_name, first_name, patronymic_name, phone_number, comment]


def import_data(data):
    with open("phonebook.csv", "a") as file:
        file.write(",".join(data))
        file.write(f"\n")


def export_data(data, filename):
    with open(filename, "w") as file:
        for rec in data:
            file.write(",".join(rec))
            file.write("\n")


def output_data():
    data = []
    with open("phonebook.csv", "r") as file:
        for line in file:
            data.append(line.strip().split(","))
    return data


def print_data(data):
    if len(data) > 0:
        print()
        print("Фамилия".center(15), "Имя".center(15), "Отчество".center(15), "Телефон".center(20),
              "Комментарий".center(20))
        print("-" * 90)
        for rec in data:
            print(rec[0].center(15), rec[1].center(15), rec[2].center(15), rec[3].center(20), rec[4].center(20))

    else:
        print("\nСправочник пуст")


def print_record(rec):
    if rec != None:
        print()
        print("Фамилия".center(15), "Имя".center(15), "Отчество".center(15), "Телефон".center(20),
              "Комментарий".center(20))
        print("-" * 90)
        print(rec[0].center(15), rec[1].center(15), rec[2].center(15), rec[3].center(20), rec[4].center(20))
    else:
        print("\nЗапись не найдена")
