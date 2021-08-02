# Задание №2
# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
# число представляется как коллекция, элементы которой это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля
# collections (пусть это и не очевидно с первого раза. Вы же не Голландец ;-).

import collections

hex_numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


'''Функция перевода шестнадцатиричного числа в десятичное'''
def hex_dec(num):
    count = len(num)
    number_dec = 0
    for i in num:
        number_dec = number_dec + hex_numbers[i] * 16 ** (count-1)
        count -= 1
    return number_dec


'''Функция перевода десятичного числа в шестнадцатиричное'''
def dec_hex(num):
    number_hex = ""
    while num != 0:
        remainder = hex_numbers[num % 16]
        number_hex = str(remainder) + number_hex
        num = int(num / 16)
    result = collections.deque(number_hex)
    return result


'''Функция перевода числа из формата коллекции в строку для красивой печати'''
def deg_str(num):
    result = ''
    for i in num:
        result += i
    return result


'''Функция сложения шестнадцатиричных чисел'''
def sum_hex(num_1, num_2):
    result = collections.deque()
    transfer = 0
    if len(num_2) > len(num_1):
        num_2, num_1 = num_1, num_2
    while num_2:
        sum_el = hex_numbers[num_1.pop()] + hex_numbers[num_2.pop()] + transfer
        result.appendleft(hex_numbers[sum_el % 16])
        if sum_el // 16 > 0:
            transfer = 1
        else:
            transfer = 0
    while num_1:
        result.appendleft(hex_numbers[hex_numbers[num_1.pop()] + transfer])
        transfer = 0
    if transfer == 1:
        result.appendleft('1')
    return result


def mult_hex(num_1, num_2):
    pass
# Не хватило времени и запутался с умножением. Разберусь и сдам со следующей домашкой.
# Очень извиняюсь, работал все выходные.


a = collections.deque(input('Введите первое шестнадцатиричное число: ').upper())
b = collections.deque(input('Введите второе шестнадцатиричное число: ').upper())
print()
print(f'Первое число: {a} или {deg_str(a)}')
print(f'Второе число: {b} или {deg_str(b)}')
print('Вариант №1')
print(f'Сумма чисел: {dec_hex(hex_dec(a) + hex_dec(b))} или {deg_str(dec_hex(hex_dec(a) + hex_dec(b)))}')
print(f'Произведение чисел: {dec_hex(hex_dec(a) * hex_dec(b))} или {deg_str(dec_hex(hex_dec(a) * hex_dec(b)))}')
print('Вариант №2')
a1 = a
a2 = a
b1 = b
b2 = b
sum_a1_b1 = sum_hex(a1, b1)
print(f'Сумма чисел: {sum_a1_b1} или {deg_str(sum_a1_b1)}')
# print(mult_hex(a2, b2))
