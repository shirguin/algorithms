# Задание №6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.

import random

a = int(input('Введите длину массива: '))
b = []
i = 1
while i <= a:
    b.append(random.randint(1, 100))
    i += 1
print(f'Сформирован массив:\n{b}')

min_el = b[0]
max_el = b[0]
ind_min_el = 0
ind_max_el = 0
i = 1
while i < len(b):
    if min_el > b[i]:
        min_el = b[i]
        ind_min_el = i
    elif max_el < b[i]:
        max_el = b[i]
        ind_max_el = i
    i += 1
print(f'Минимальный элемент: {min_el} индекс: {ind_min_el}\nМаксимальный элемент: {max_el} индекс: {ind_max_el}')
sum_numbers = 0
if ind_min_el < ind_max_el:
    sum_numbers = sum(b[(ind_min_el+1):ind_max_el])
else:
    sum_numbers = sum(b[(ind_max_el + 1):ind_min_el])

print(f'Сумма элементов, находящихся между минимальным и максимальным элементами, равна: {sum_numbers}')
print('Программа завершена.')
