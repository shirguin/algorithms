# Задание №1
# Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков. Проанализировать
# результат и определить программы с наиболее эффективным использованием
# памяти.


# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''
# Вариант 1
number = int(input('Введите трехзначное число: '))
a = number // 100
b = (number % 100) // 10
c = number % 10
summa = a + b + c
result = a * b * c
print(f"Сумма цифр числа {number}: {summa}")
print(f'Произведение цифр числа {number}: {result}')

# Вариант 2
number = input('Введите трехзначное число: ')
summa = 0
result = 1
for i in number:
    summa = summa + int(i)
    result = result * int(i)
print(f"Сумма цифр числа {number}: {summa}")
print(f'Произведение цифр числа {number}: {result}')
'''

# Считаем Вариант 1:
# number = 12
# a = 12
# b = 12
# c = 12
# summa = 12
# result = 12
# Для 32 bit машины получается 6 переменных(int) 6 * 12 = 72 байта
# Для 64 bit машины получается 6 переменных(int) 6 * 24 = 144 байта

# Считаем Вариант 2:
# number = 12
# summa = 12
# result = 12
# i = 12
# Для 32 bit машины получается 6 переменных(int) 4 * 12 = 48 байт
# Для 64 bit машины получается 6 переменных(int) 4 * 24 = 96 байт

# Вывод: Второй вариант более эфективно использует память.


# 2. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из
#    чисел в диапазоне от 2 до 9.

'''
i = 2
list_result = []
while i <= 9:
    count = 0
    n = 2
    list_temp = []
    while n <= 99:
        if n % i == 0:
            count += 1
        n += 1
    list_temp = [i, count]
    list_result.append(list_temp)
    i += 1
print('Кратность чисел от 2 до 9 в диапазоне чисел от 2 до 99:')
el = 0
while el < len(list_result):
    print(f'числу {list_result[el][0]} кратно {list_result[el][1]} чисел')
    el += 1
print(f'\nПрограмма завершена.')
'''

# Считаем для 32 bit:
# i = 12
# count = 12
# n = 12
# el = 12
# list_temp = [9, 11]
# list_temp = 20 + 4 * 2 = 28
# list_result = [[2, 49], [3, 33], [4, 24], [5, 19], [6, 16], [7, 14], [8, 12], [9, 11]]
# list_result = 20 + 4 * 8 * 28 = 916
# Всего для переменных понадобится 4 * 12 + 28 + 916 = 992 байт

# Считаем для 64 bit:
# i = 24
# count = 24
# n = 24
# el = 24
# list_temp = [9, 11]
# list_temp = 40 + 8 * 2 = 56
# list_result = [[2, 49], [3, 33], [4, 24], [5, 19], [6, 16], [7, 14], [8, 12], [9, 11]]
# list_result = 40 + 8 * 8 * 56 = 3624
# Всего для переменных понадобится 4 * 24 + 56 + 3624 = 3776 байт / 1024 = 3,69 мегабайт

# 3. Посчитать четные и нечетные цифры введенного натурального числа. Например, если
#    введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

"""
# Вариант №1
number = input('Введите натуральное число: ')
even_numbers = 0
even_numbers_str = ''
odd_numbers = 0
odd_numbers_str = ''
for el in number:
    if int(el) % 2 == 0 or int(el) == 0:
        even_numbers += 1
        even_numbers_str += f', {el}'
    else:
        odd_numbers += 1
        odd_numbers_str += f', {el}'
print(f'В числе {number} {even_numbers} четных цифр ({even_numbers_str[2:]}) и {odd_numbers} нечетных цифр ({odd_numbers_str[2:]})')
print('Программа завершена.')

# Вариант №2
number = input('Введите натуральное число: ')
even_numbers = []
odd_numbers = []
for el in number:
    if int(el) % 2 == 0 or el == '0':
        even_numbers.append(el)
    else:
        odd_numbers.append(el)
print(f'В числе {number} {len(even_numbers)} четных цифр {even_numbers} и {len(odd_numbers)} нечетных цифр {odd_numbers}')
print('Программа завершена')
"""

# Для подсчета установим, что число введенное пользователем не может содержать больше 5 цифр,
# а также число может состоять только из четных или не четных цифр.

# Считаем Вариант 1 для 32 bit:
# number(str) = 21 + 5 = 26
# even_numbers(int) = 12
# even_numbers_str = ', 2, 4, 6, 8, 4'
# even_numbers_str(str) = 21 + 15 = 36
# odd_numbers(int) = 12
# odd_numbers_str = ', 1, 3, 5, 7, 9'
# odd_numbers_str(str) = 21 + 15 = 36
# el(int) = 12
# ИТОГО: 26 + 12 + 36 + 12 + 36 + 12 = 134 байта

# Считаем Вариант 1 для 64 bit:
# number(str) = 37 + 5 = 42
# even_numbers(int) = 24
# even_numbers_str = ', 2, 4, 6, 8, 4'
# even_numbers_str(str) = 37 + 15 = 52
# odd_numbers(int) = 24
# odd_numbers_str = ', 1, 3, 5, 7, 9'
# odd_numbers_str(str) = 37 + 15 = 52
# el(int) = 24
# ИТОГО: 42 + 24 + 52 + 24 + 52 + 24 = 218 байт

# Считаем Вариант 2 для 32 bit:
# number(str) = 21 + 5 = 26
# even_numbers = ['2', '4', '6', '8', '4']
# even_numbers(list) = 20 + 4 * 5 * (21 + 1) = 460
# odd_numbers = ['1', '3', '5', '7', '9']
# odd_numbers(list) = 20 + 4 * 5 * (21 + 1) = 460
# el(int) = 12
# ИТОГО: 26 + 460 + 460 + 12 = 958 байт

# Считаем Вариант 2 для 64 bit:
# number(str) = 37 + 5 = 42
# even_numbers = ['2', '4', '6', '8', '4']
# even_numbers(list) = 40 + 8 * 5 * (37 + 1) = 1560
# odd_numbers = ['1', '3', '5', '7', '9']
# odd_numbers(list) = 40 + 8 * 5 * (37 + 1) = 1560
# el(int) = 24
# ИТОГО: 42 + 1560 + 1560 + 24 = 3186 байт / 1024 = 3,12 мегабайт

# Вывод: первый вариант более эфективно использует память.
