# Задание №7
# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
# как равны между собой (оба являться минимальными), так и различаться.

import random

a = int(input('Введите длину массива: '))
b = []
i = 1
while i <= a:
    b.append(random.randint(1, 100))
    i += 1
print(f'Сформирован массив:\n{b}')

if b[0] <= b[1]:
    index_min_1 = 0
    index_min_2 = 1
else:
    index_min_1 = 1
    index_min_2 = 0

for i in range(2, len(b)):
    if b[i] < b[index_min_1]:
        c = index_min_1
        index_min_1 = i
        if b[c] < b[index_min_2]:
            index_min_2 = c
    elif b[i] < b[index_min_2]:
        index_min_2 = i

print(f'Минимальный элемент массива №1: {b[index_min_1]} индекс [{index_min_1}]')
print(f'Минимальный элемент массива №2: {b[index_min_2]} индекс [{index_min_2}]')
print('Программа завершена.')
