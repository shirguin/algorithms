# Задание №4
# Написать программу, которая генерирует в указанных пользователем границах
# случайное целое число,
# случайное вещественное число,
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если
# надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна
# вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

type_range = input('Введите тип данных для диапазона генерации "int", "float", "str": ')
while type_range not in ('int', 'float', 'str'):
    print('Не правильно введен тип данных')
    type_range = input('Введите тип данных для диапазона генерации "int", "float", "str": ')

start_range = input('Введите начало диапазона: ')
end_range = input('Введите конец диапазона: ')

if type_range == 'int':
    result = random.randint(int(start_range), int(end_range))
elif type_range == 'float':
    result = round(random.uniform(float(start_range), float(end_range)), 2)
else:
    result = chr(random.randint(ord(start_range), ord(end_range)))

print(f'Результат random генерации в диапазоне ({start_range} - {end_range}) равен {result}')
