def calculate_rational(numbers, math_symbol):
    try:
        a = int(numbers[0])
        b = int(numbers[1])
    except ValueError:
        a = float(numbers[0])
        b = float(numbers[1])
    if math_symbol == "+":
        return a + b
    elif math_symbol == "-":
        return a - b
    elif math_symbol == "*":
        return a * b
    elif math_symbol == "/" and b != 0:
        return a / b
    elif math_symbol == "**":
        return a ** b


def calculate_complex(numbers, math_symbol):
    real_number1 = float(numbers[0])
    imaginary_unit1 = float(numbers[1])
    a = complex(real_number1, imaginary_unit1)
    real_number2 = float(numbers[2])
    imaginary_unit2 = float(numbers[3])
    b = complex(real_number2, imaginary_unit2)
    if math_symbol == "+":
        return a + b
    elif math_symbol == "-":
        return a - b
    elif math_symbol == "*":
        return a * b
    elif math_symbol == "/" and b != 0:
        return a / b
    elif math_symbol == "**":
        return a ** b
