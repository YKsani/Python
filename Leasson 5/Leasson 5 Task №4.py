# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def file_write(name, s):
    with open(name, 'w') as data:
        data.write(s)


def file_read(name):
    with open(name, "r") as data:
        return data.read()


def coding(txt):
    result = ''
    prev_char = ''
    count = 1
    for char in txt:
        if char != prev_char:
            if prev_char:
                result += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    result += str(count) + prev_char
    return result


def decoding(txt):
    count = ''
    result = ''
    for char in txt:
        if char.isdigit():
            count += char
        else:
            result += char * int(count)
            count = ''
    return result


file_decode: str = "file_decode.txt"
file_encode: str = "file_encode.txt"

text_encode = "dsadsssswwqqqqquuuudsssssssswwwwwwwqqqqqqq"
print(f'Входные данные: {text_encode} \n')


file_write(file_decode, coding(text_encode))
text = file_read(file_decode)
len_text_decode = len(text)
print(f"Текст после сжатия данных: {text}")

file_write(file_encode, decoding(text))
text = file_read(file_encode)
len_text_encode = len(text)
print(f"Текст после восстановления данных: {text}")
print(f'Сжато на {round(len_text_decode / len_text_encode *100 - 100) * -1}%')