# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def input_values():
    xy = ["X", "Y"]
    coordinats = []
    for i in range(2):
        correct_value = False
        while not correct_value:
            try:
                coordinats.append(int(input(f"Введите координату по {xy[i]}: ")))
                correct_value = True
            except ValueError:
                print("Ошибка: Введено не корректное значение")
    return coordinats


def calculate_values(a, b):
    result = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return result


print(f'Введите координаты точки А' '\n')
point_a = input_values()
print()
print(f'Введите координаты точки B' '\n')
point_b = input_values()
print()

print(f"Длина отрезка: {format(calculate_values(point_a, point_b), '.2f')}")