# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def calculate_values(list):
    s: str = ""
    for i in range(len(list)):
        if i < len(list) - 2:
            if list[i] > 1:
                s += f"{list[i]}x^{len(list) - i - 1}"
            elif list[i] == 1:
                s += f"x^{len(list) - i - 1}"
            if list[i + 1] != 0:
                s += " + "
        elif i == len(list) - 2:
            if list[i] > 1:
                s += f"{list[i]}x"
            elif list[i] == 1:
                s += f"x"
            if list[i + 1] != 0:
                s += " + "
        elif i == len(list) - 1:
            if list[i] >= 1:
                s += f"{list[i]}"
    s += " = 0"
    return s


def get_degree(d):
    if "x^" in d:
        i = d.find("^")
        num = int(d[i + 1:])
    elif ("x" in d) and ("^" not in d):
        num = 1
    else:
        num = -1
    return num


def get_coef(c):
    if "x" in c:
        i = c.find("x")
        if i != 0:
            num = int(c[:i])
        else:
            num = 1
    return num


def get_polynomial(s):
    s = s[0].replace(" ", "").split("=")
    s = s[0].split("+")
    polynomial_list = []
    polynomial_list_len = len(s)
    if get_degree(s[-1]) == -1:
        polynomial_list.append(int(s[-1]))
        polynomial_list_len -= 1
    i = 1
    j = polynomial_list_len - 1
    while j >= 0:
        if get_degree(s[j]) != -1 and get_degree(s[j]) == i:
            polynomial_list.append(get_coef(s[j]))
            j -= 1
            i += 1
        else:
            polynomial_list.append(0)
            i += 1
    return polynomial_list


def parse_polynomial():
    polynomial_list_1 = get_polynomial(list_coefficients_1)
    polynomial_list_2 = get_polynomial(list_coefficients_2)
    lst_len = len(polynomial_list_1)
    if len(polynomial_list_1) > len(polynomial_list_2):
        lst_len = len(polynomial_list_2)
    lst_new = [polynomial_list_1[i] + polynomial_list_2[i] for i in range(lst_len)]
    if len(polynomial_list_1) > len(polynomial_list_2):
        for i in range(lst_len, len(polynomial_list_1)):
            lst_new.append(polynomial_list_1[i])
    else:
        for i in range(lst_len, len(polynomial_list_2)):
            lst_new.append(polynomial_list_2[i])
    lst_new.reverse()
    return lst_new


def file_write(name, s):
    with open(name, "w", encoding="utf-8") as data:
        data.write(s)


def file_read(name):
    with open(name, "r", encoding="utf-8") as data:
        pulynomial_list = data.readlines()
    return pulynomial_list


file1_name: str = "polynomial_1.txt"
file2_name: str = "polynomial_2.txt"
file_result_name: str = "file_task№5.txt"

list_coefficients_1 = file_read(file1_name)
list_coefficients_2 = file_read(file2_name)
modified_list_1 = ", ".join(map(str, list_coefficients_1))
modified_list_2 = ", ".join(map(str, list_coefficients_2))

print(f"В первом файле следующий многочлен: {modified_list_1}")
print(f"Во втором файле следующий многочлен: {modified_list_2}")

list_coefficients_result = parse_polynomial()
file_write(file_result_name, calculate_values(list_coefficients_result))

list_from_file_result = ", ".join(map(str, file_read(file_result_name)))
print(f"\nСумма многочленов = {list_from_file_result}")
