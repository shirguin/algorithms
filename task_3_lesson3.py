# Задание №3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

b[ind_min_el] = max_el
b[ind_max_el] = min_el
print(f'Поменяли элементы местами\n{b}')
print('Программа завершена.')
