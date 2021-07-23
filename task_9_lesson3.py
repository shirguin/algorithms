# Задание №9
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

# Формируем матрицу
a = int(input('Введите ширину матрицы: '))
b = int(input('Введите высоту матрицы: '))
list_data = []
i = b
while i > 0:
    ls = []
    i1 = a
    while i1 > 0:
        ls.append(random.randint(1, 100))
        i1 -= 1
    list_data.append(ls)
    i -= 1
# Выводим матрицу на экран
el1 = 0
while el1 < len(list_data):
    el2 = 0
    while el2 < len(list_data[el1]):
        print(f'{list_data[el1][el2]:5}', end='   ')
        el2 += 1
    print()
    el1 += 1
# Ищем минимальные элементы по столбцам
ls_min = []
i = 0
while i < a:
    i1 = 0
    number_min = list_data[i1][i]
    while i1 < b - 1:
        if number_min > list_data[i1+1][i]:
            number_min = list_data[i1+1][i]
        i1 += 1
    ls_min.append(number_min)
    i += 1
# Выводим результат
print(f'Минимальные значения по столбцам матрицы\n{ls_min}')
print(f'максимальный элемент среди минимальных элементов столбцов матрицы равен: {max(ls_min)}')
print('Программа завершена.')
