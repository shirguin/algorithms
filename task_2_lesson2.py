# Задание №2
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

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
"""
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