# Задание №5
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию (индекс) в массиве.

import random

a = int(input('Введите длину массива: '))
b = []
i = 1
while i <= a:
    b.append(random.randint(-50, 50))
    i += 1
print(f'Сформирован массив:\n{b}')

index = -1
i = 0
while i < len(b):
    if b[i] < 0 and index == -1:
        index = i
    elif 0 > b[i] > b[index]:
        index = i
    i += 1

print(f'В этом массиве максимальный отрицательный элемент равен {b[index]}, его индекс равен {index}')
print('Программа завершена.')
