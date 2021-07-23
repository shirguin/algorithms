# Задание №4
# Определить, какое число в массиве встречается чаще всего.

import random

a = int(input('Введите длину массива: '))
b = []
i = 1
while i <= a:
    b.append(random.randint(1, 100))
    i += 1
print(f'Сформирован массив:\n{b}')

max_count_number = b[0]
i = 1
while i < len(b):
    if b.count(max_count_number) < b.count(b[i]):
        max_count_number = b[i]
    i += 1

print(f'В этом массиве чаще всего ({b.count(max_count_number)} раза) встречается число {max_count_number}')
print('Программа завершена.')
