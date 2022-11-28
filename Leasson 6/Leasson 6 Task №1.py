# Формат: Объясняет преподаватель
#
# Задача: предложить улучшения кода для уже решённых задач:
#
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# доска будет задана через список

text = 'Напишите абв напиабв програбвмму программу, удаляющую из абв текста все вабвс слова, содерабващие содержащие "абв"'
print(f'{text} \n')

def del_some_words(my_text):
    new_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(new_text)

new_text = del_some_words(text)
print(f'Результат работы программы: {new_text}')